# Procurement and cartel screening data for Chapter 5 (cartels)
#
# Real data:
#   data/raw/worldbank_procurement.csv     -- World Bank Major Contract Awards
#   data/derived/procurement_award_hhi.csv -- supplier award-concentration screen
#
# Synthetic (illustrative, clearly labelled): the bid-ROTATION screen needs
# bid-level data (every bidder on every tender, not just the winner). Open
# procurement portals publish award records, not losing bids, so the cement
# bid-rotation example stays synthetic until a competition authority supplies
# bid-level data. The file schema below is what chapters/05-cartels.qmd reads;
# drop a real bid-level file at data/derived/cartel_cement_bids.csv with the
# same columns to swap it in.

library(dplyr)
library(tidyr)
library(readr)
library(httr)
library(jsonlite)
library(lubridate)

dir.create("data/raw", recursive = TRUE, showWarnings = FALSE)
dir.create("data/derived", recursive = TRUE, showWarnings = FALSE)

status <- list(worldbank = "not attempted", award_hhi = "not attempted")

# ============================================================================
# 1. World Bank Major Contract Awards (real, open Socrata endpoint, no key)
# ============================================================================

wb_base <- "https://finances.worldbank.org/resource/kdui-wcs3.json"

fetch_worldbank <- function() {
  rows <- list()
  offset <- 0L
  page <- 50000L
  repeat {
    q <- paste0(wb_base,
                "?$limit=", page,
                "&$offset=", offset,
                "&$where=", URLencode("fiscal_year>='2015'"),
                "&$order=fiscal_year")
    resp <- GET(q, timeout(120))
    if (status_code(resp) != 200) {
      stop("HTTP ", status_code(resp))
    }
    chunk <- content(resp, as = "text", encoding = "UTF-8") |>
      fromJSON(flatten = TRUE)
    # fromJSON may return a list/NULL on an unexpected payload; guard before nrow()
    # so the loop breaks safely instead of erroring on logical(0).
    if (is.null(chunk) || !is.data.frame(chunk) || nrow(chunk) == 0) break
    rows[[length(rows) + 1]] <- as_tibble(chunk)
    if (nrow(chunk) < page) break
    offset <- offset + page
  }
  bind_rows(rows)
}

wb_clean <- tryCatch(
  {
    cat("Querying World Bank procurement data ...\n")
    raw <- fetch_worldbank()
    raw |>
      mutate(
        contract_amount = suppressWarnings(as.numeric(total_contract_amount)),
        fiscal_year = suppressWarnings(as.integer(fiscal_year))
      ) |>
      filter(!is.na(contract_amount), contract_amount > 0)
  },
  error = function(e) {
    message("  World Bank API failed (", conditionMessage(e), ")")
    NULL
  }
)

if (!is.null(wb_clean) && nrow(wb_clean) > 0) {
  write_csv(wb_clean, "data/raw/worldbank_procurement.csv")
  status$worldbank <- "real (World Bank Major Contract Awards)"
  cat("✓ World Bank procurement saved:", nrow(wb_clean), "contracts\n")

  # --- Real supplier award-concentration screen --------------------------
  # HHI of award value by supplier within borrower_country x category x year.
  # A legitimate structural screen: persistently high concentration in public
  # tenders is one (weak) flag among the OECD cartel-screen battery.
  supplier_col <- intersect(c("supplier", "supplier_name"), names(wb_clean))[1]
  cat_col <- intersect(c("procurement_category", "procurement_type",
                         "major_sector"), names(wb_clean))[1]
  geo_col <- intersect(c("borrower_country", "country", "region"),
                       names(wb_clean))[1]

  if (!is.na(supplier_col) && !is.na(cat_col) && !is.na(geo_col)) {
    award_hhi <- wb_clean |>
      transmute(
        geo = .data[[geo_col]],
        category = .data[[cat_col]],
        fiscal_year = fiscal_year,
        supplier = .data[[supplier_col]],
        contract_amount = contract_amount
      ) |>
      filter(!is.na(supplier), !is.na(category), !is.na(geo)) |>
      group_by(geo, category, fiscal_year, supplier) |>
      summarise(supplier_value = sum(contract_amount), .groups = "drop_last") |>
      mutate(
        group_value = sum(supplier_value),
        share = supplier_value / group_value
      ) |>
      summarise(
        n_suppliers = n(),
        group_award_value = first(group_value),
        hhi = sum(share^2) * 10000,
        .groups = "drop"
      ) |>
      filter(n_suppliers >= 5) |>   # only groups with enough suppliers to mean anything
      arrange(desc(hhi)) |>
      mutate(data_source = "real")

    write_csv(award_hhi, "data/derived/procurement_award_hhi.csv")
    status$award_hhi <- "real (derived from World Bank awards)"
    cat("✓ Award-concentration screen saved:", nrow(award_hhi), "market-years\n")
  } else {
    status$award_hhi <- "skipped (expected columns absent)"
    cat("⚠ World Bank schema changed; skipped award-HHI derivation.\n")
  }
} else {
  status$worldbank <- "MISSING (World Bank API unreachable)"
  # Synthetic fallback for the award screen so Chapter 5 renders offline.
  # Tagged synthetic via data_source so the figure caption can say so.
  set.seed(123)
  geos <- c("Kenya", "Colombia", "India", "Indonesia", "Vietnam",
            "Bangladesh", "Nigeria", "Mexico")
  categories <- c("Civil Works", "Consultant Services", "Goods", "Technical Services")
  synth_hhi <- expand_grid(geo = geos, category = categories,
                           fiscal_year = 2015:2023) |>
    mutate(
      n_suppliers = sample(5:15, n(), replace = TRUE),
      group_award_value = round(rlnorm(n(), meanlog = 15, sdlog = 1.5)),
      hhi = pmax(500, pmin(10000, rnorm(n(), mean = 2200, sd = 1200))),
      data_source = "synthetic_fallback"
    ) |>
    arrange(desc(hhi))
  write_csv(synth_hhi, "data/derived/procurement_award_hhi.csv")
  status$award_hhi <- "SYNTHETIC fallback (World Bank API unreachable)"
  cat("⚠ World Bank procurement not pulled; wrote SYNTHETIC fallback for ",
      "procurement_award_hhi.csv so Chapter 5 still renders. Re-run with ",
      "network access to replace it with real data.\n", sep = "")
}

# ============================================================================
# 2. Cartel bid-rotation example (SYNTHETIC, illustrative)
#    Consumed by chapters/05-cartels.qmd (CV and transition-matrix screens).
#    Schema: project_id, date, year, cartel_period, winner, base_cost,
#            markup, winning_bid
# ============================================================================

set.seed(123)
n_projects <- 200
firms <- c("Firm_A", "Firm_B", "Firm_C", "Firm_D")

cement_bids <- tibble(
  project_id = 1:n_projects,
  date = seq(as.Date("2010-01-01"), by = "month", length.out = n_projects),
  year = year(date)
) |>
  mutate(
    cartel_period = year >= 2014 & year <= 2018,
    winner = if_else(
      cartel_period,
      firms[(project_id %% length(firms)) + 1],          # systematic rotation
      sample(firms, n(), replace = TRUE, prob = c(0.3, 0.25, 0.25, 0.2))
    ),
    base_cost = rnorm(n(), 500000, 100000),
    markup = if_else(cartel_period,
                     rnorm(n(), 0.25, 0.05),               # compressed, high
                     rnorm(n(), 0.10, 0.08)),              # competitive
    winning_bid = base_cost * (1 + markup)
  )

write_csv(cement_bids, "data/derived/cartel_cement_bids.csv")
cat("✓ Synthetic cement bid-rotation example written (illustrative).\n")

# ============================================================================
# Metadata
# ============================================================================

metadata <- tibble(
  dataset = c("worldbank_procurement", "procurement_award_hhi", "cartel_cement_bids"),
  file = c("data/raw/worldbank_procurement.csv",
           "data/derived/procurement_award_hhi.csv",
           "data/derived/cartel_cement_bids.csv"),
  source = c("World Bank Major Contract Awards",
             "Derived from World Bank awards",
             "Synthetic (illustrative)"),
  chapter_use = c("Ch05", "Ch05", "Ch05"),
  status = c(status$worldbank, status$award_hhi, "synthetic — no open bid-level source"),
  notes = c("Real award records, 2015+.",
            "Supplier HHI by country x category x year (structural screen).",
            "Bid-rotation/CV screens need every bidder's bid; swap in real bid-level data when available."),
  date_created = Sys.Date()
)
write_csv(metadata, "data/raw/procurement_cartels_metadata.csv")

cat("\n--- Procurement / cartel collection summary ---\n")
cat("  World Bank awards :", status$worldbank, "\n")
cat("  Award HHI screen  :", status$award_hhi, "\n")
cat("  Cement bids       : synthetic (illustrative)\n")
