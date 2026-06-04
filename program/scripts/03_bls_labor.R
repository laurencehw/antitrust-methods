# BLS labor market data for Chapter 10 (labor markets)
# Produces two real-data files consumed by chapters/10-labor-markets.qmd:
#   data/raw/bls_industry_employment.csv  -- CES industry employment (BLS API)
#   data/raw/qcew_county_employment.csv   -- QCEW county employment for HHI proxy
# Each pull degrades gracefully to a clearly-labelled synthetic fallback with the
# SAME schema, so the book still renders offline. Status is recorded in metadata.
#
# Requires BLS_KEY in .Renviron for the CES API pull (register at
# https://data.bls.gov/registrationEngine/). The QCEW download is an open bulk
# file and needs no key.

library(dplyr)
library(tidyr)
library(readr)
library(stringr)
library(lubridate)

dir.create("data/raw", recursive = TRUE, showWarnings = FALSE)
dir.create("data/derived", recursive = TRUE, showWarnings = FALSE)

# Tracks whether each source landed real data or a synthetic fallback.
status <- list(ces = "not attempted", qcew = "not attempted")

# ============================================================================
# 1. CES national employment by major industry (BLS API, real)
# ============================================================================

industry_series <- c(
  "CES0000000001",  # Total nonfarm
  "CES4142000001",  # Retail trade
  "CES4300000001",  # Transportation & warehousing
  "CES5000000001",  # Information
  "CES5500000001",  # Financial activities
  "CES6000000001",  # Professional & business services
  "CES6500000001",  # Education & health services
  "CES7000000001",  # Leisure & hospitality
  "CES0800000001"   # Other services
)

start_year <- year(Sys.Date()) - 15
end_year   <- year(Sys.Date())

ces_data <- NULL
if (requireNamespace("blscrapeR", quietly = TRUE) &&
    nchar(Sys.getenv("BLS_KEY")) > 0) {
  ces_data <- tryCatch(
    lapply(industry_series, function(series) {
      tryCatch(
        blscrapeR::bls_api(series,
                           startyear = start_year,
                           endyear   = end_year,
                           registrationKey = Sys.getenv("BLS_KEY")),
        error = function(e) {
          message("  CES: could not fetch ", series, " (", conditionMessage(e), ")")
          NULL
        }
      )
    }) |>
      bind_rows(),
    error = function(e) NULL
  )
}

if (!is.null(ces_data) && nrow(ces_data) > 0) {
  # bls_api() returns columns: year, period, periodName, value, seriesID
  write_csv(ces_data, "data/raw/bls_industry_employment.csv")
  status$ces <- "real (BLS CES API)"
  cat("✓ CES industry employment saved:", nrow(ces_data), "rows\n")
} else {
  status$ces <- "MISSING (set BLS_KEY and install blscrapeR)"
  cat("⚠ CES employment not pulled. Set BLS_KEY in .Renviron and ",
      "install.packages('blscrapeR'). Chapter 10's CES figure will show a ",
      "graceful 'data not available' message.\n", sep = "")
}

# ============================================================================
# 2. QCEW county employment for the employer-concentration proxy (open bulk)
# ============================================================================
#
# The chapter computes HHI proxy = 10,000 / (private establishments per county)
# from county-level, total-all-industries rows. In QCEW that is:
#   agglvl_code == 70  (county, total, by ownership sector)
#   own_code     == 5  (private)
#   industry_code == "10" (total, all industries)
# We keep exactly the columns chapters/10-labor-markets.qmd reads.

qcew_years <- 2021:2023  # panel; the chapter cross-section uses year == 2023

qcew_cols <- cols_only(
  area_fips        = col_character(),
  own_code         = col_integer(),
  industry_code    = col_character(),
  agglvl_code      = col_integer(),
  year             = col_integer(),
  annual_avg_estabs = col_double(),
  annual_avg_emplvl = col_double(),
  total_annual_wages = col_double(),
  annual_avg_wkly_wage = col_double()
)

download_qcew_year <- function(yr) {
  url <- sprintf(
    "https://data.bls.gov/cew/data/files/%d/csv/%d_annual_singlefile.zip",
    yr, yr
  )
  zip_path <- tempfile(fileext = ".zip")
  on.exit(unlink(zip_path), add = TRUE)
  # QCEW can be slow; allow a generous timeout.
  old_to <- options(timeout = 600); on.exit(options(old_to), add = TRUE)
  utils::download.file(url, zip_path, mode = "wb", quiet = TRUE)

  inner <- utils::unzip(zip_path, list = TRUE)$Name[1]
  con <- unz(zip_path, inner)
  df <- readr::read_csv(con, col_types = qcew_cols, progress = FALSE)

  df |>
    filter(agglvl_code == 70, own_code == 5, industry_code == "10",
           annual_avg_estabs > 0, annual_avg_emplvl > 0)
}

qcew <- tryCatch(
  {
    out <- lapply(qcew_years, function(yr) {
      message("  QCEW: downloading ", yr, " annual singlefile ...")
      download_qcew_year(yr)
    }) |>
      bind_rows()
    if (nrow(out) == 0) stop("no county rows after filtering")
    out
  },
  error = function(e) {
    message("  QCEW download failed (", conditionMessage(e), ")")
    NULL
  }
)

if (!is.null(qcew) && nrow(qcew) > 0) {
  write_csv(qcew, "data/raw/qcew_county_employment.csv")
  status$qcew <- "real (BLS QCEW annual singlefile)"
  cat("✓ QCEW county employment saved:", nrow(qcew), "county-year rows\n")
} else {
  # ---- Synthetic fallback: SAME schema as the real file -------------------
  # Lognormal establishment counts reproduce the real urban/rural spread
  # (a few rural counties with tens of establishments -> high HHI proxy;
  # large urban counties with thousands -> low HHI proxy). Clearly labelled.
  set.seed(123)
  fips <- maps::county.fips$fips |> unique()
  fips <- str_pad(as.character(fips), 5, pad = "0")

  synth <- expand_grid(area_fips = fips, year = qcew_years) |>
    mutate(
      own_code      = 5L,
      industry_code = "10",
      agglvl_code   = 70L,
      annual_avg_estabs = pmax(10, round(rlnorm(n(), meanlog = 6, sdlog = 1.4))),
      annual_avg_emplvl = round(annual_avg_estabs *
                                  pmax(3, rlnorm(n(), meanlog = 2.3, sdlog = 0.6))),
      annual_avg_wkly_wage = round(rnorm(n(), 1050, 220)),
      total_annual_wages = round(annual_avg_emplvl * annual_avg_wkly_wage * 52)
    ) |>
    select(area_fips, own_code, industry_code, agglvl_code, year,
           annual_avg_estabs, annual_avg_emplvl,
           total_annual_wages, annual_avg_wkly_wage)

  write_csv(synth, "data/raw/qcew_county_employment.csv")
  status$qcew <- "SYNTHETIC fallback (QCEW download unavailable)"
  cat("⚠ QCEW download unavailable; wrote SYNTHETIC fallback with the ",
      "real schema so Chapter 10 still renders. Re-run with network access to ",
      "replace it with real data.\n", sep = "")
}

# ============================================================================
# Metadata
# ============================================================================

metadata <- tibble(
  dataset = c("bls_industry_employment", "qcew_county_employment"),
  file = c("data/raw/bls_industry_employment.csv",
           "data/raw/qcew_county_employment.csv"),
  source = c("BLS Current Employment Statistics (API)",
             "BLS Quarterly Census of Employment and Wages (bulk)"),
  chapter_use = c("Ch10", "Ch10"),
  status = c(status$ces, status$qcew),
  notes = c("National employment by major industry, monthly.",
            "County total-private establishments & employment; feeds HHI proxy."),
  date_created = Sys.Date()
)
write_csv(metadata, "data/raw/bls_metadata.csv")

cat("\n--- BLS / QCEW collection summary ---\n")
cat("  CES employment :", status$ces, "\n")
cat("  QCEW counties  :", status$qcew, "\n")
