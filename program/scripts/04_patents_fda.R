# Patent and FDA data for Chapter 11 (Innovation & IP)
# PatentsView API + FDA Orange Book
# Author: Automated data collection script
# Date: 2025-11-24

library(dplyr)
library(tidyr)
library(readr)
library(httr)
library(jsonlite)
library(lubridate)

# ============================================================================
# Phase 1: PatentsView API
# ============================================================================

# PatentsView API documentation: https://patentsview.org/apis/api

# Helper function to query PatentsView
query_patents <- function(query_params, endpoint = "patents") {
  base_url <- paste0("https://api.patentsview.org/", endpoint, "/query")
  
  response <- POST(
    base_url,
    body = query_params,
    encode = "json",
    add_headers("Content-Type" = "application/json")
  )
  
  if (status_code(response) == 200) {
    content(response, as = "parsed")
  } else {
    cat("API error:", status_code(response), "\n")
    NULL
  }
}

# ============================================================================
# Query 1: Pharmaceutical patents (last 15 years)
# ============================================================================

pharma_query <- list(
  q = list(
    `_and` = list(
      list(`_gte` = list(patent_date = "2010-01-01")),
      list(`_lte` = list(patent_date = as.character(Sys.Date()))),
      list(`_or` = list(
        list(cpc_subgroup_id = "A61K"),  # Pharma preparations
        list(cpc_subgroup_id = "A61P"),  # Therapeutic activity
        list(cpc_subgroup_id = "C07D")   # Heterocyclic compounds
      ))
    )
  ),
  f = c("patent_id", "patent_number", "patent_title", "patent_date", 
        "patent_year", "assignee_organization", "cpc_subgroup_id",
        "cited_patent_count", "citedby_patent_count"),
  o = list(per_page = 10000)
)

cat("Querying PatentsView for pharmaceutical patents...\n")
pharma_patents <- query_patents(pharma_query)

if (!is.null(pharma_patents)) {
  pharma_df <- pharma_patents$patents %>%
    bind_rows() %>%
    as_tibble()
  
  write_csv(pharma_df, "data/raw/patents_pharma.csv")
  cat("✓ Pharmaceutical patents saved:", nrow(pharma_df), "records\n")
} else {
  cat("⚠ PatentsView API call failed\n")
}

# ============================================================================
# Query 2: Tech/software patents (for digital markets context)
# ============================================================================

tech_query <- list(
  q = list(
    `_and` = list(
      list(`_gte` = list(patent_date = "2010-01-01")),
      list(`_lte` = list(patent_date = as.character(Sys.Date()))),
      list(`_or` = list(
        list(cpc_subgroup_id = "G06F"),  # Computer systems
        list(cpc_subgroup_id = "G06Q"),  # Data processing for business
        list(cpc_subgroup_id = "H04L")   # Transmission of digital info
      ))
    )
  ),
  f = c("patent_id", "patent_number", "patent_title", "patent_date", 
        "patent_year", "assignee_organization", "cpc_subgroup_id",
        "cited_patent_count", "citedby_patent_count"),
  o = list(per_page = 10000)
)

cat("Querying PatentsView for tech/software patents...\n")
tech_patents <- query_patents(tech_query)

if (!is.null(tech_patents)) {
  tech_df <- tech_patents$patents %>%
    bind_rows() %>%
    as_tibble()
  
  write_csv(tech_df, "data/raw/patents_tech.csv")
  cat("✓ Tech patents saved:", nrow(tech_df), "records\n")
} else {
  cat("⚠ PatentsView API call failed\n")
}

# ============================================================================
# Phase 2: FDA Orange Book
# ============================================================================

# FDA Orange Book data files
# Source: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files

fda_base_url <- "https://www.accessdata.fda.gov/cder/ob/docs/queryai.zip"

# Download and extract Orange Book data
cat("Downloading FDA Orange Book data...\n")

temp_zip <- tempfile(fileext = ".zip")
temp_dir <- tempdir()

tryCatch({
  download.file(fda_base_url, temp_zip, mode = "wb", quiet = TRUE)
  unzip(temp_zip, exdir = temp_dir)
  
  # Read key files
  # products.txt: Approved drug products
  # patent.txt: Patent information
  # exclusivity.txt: Exclusivity data
  
  products_file <- file.path(temp_dir, "products.txt")
  patent_file <- file.path(temp_dir, "patent.txt")
  exclusivity_file <- file.path(temp_dir, "exclusivity.txt")
  
  if (file.exists(products_file)) {
    products <- read_delim(products_file, delim = "~", 
                          col_types = cols(.default = "c"),
                          show_col_types = FALSE)
    write_csv(products, "data/raw/fda_products.csv")
    cat("✓ FDA products saved:", nrow(products), "records\n")
  }
  
  if (file.exists(patent_file)) {
    patents <- read_delim(patent_file, delim = "~",
                         col_types = cols(.default = "c"),
                         show_col_types = FALSE)
    write_csv(patents, "data/raw/fda_patents.csv")
    cat("✓ FDA patents saved:", nrow(patents), "records\n")
  }
  
  if (file.exists(exclusivity_file)) {
    exclusivity <- read_delim(exclusivity_file, delim = "~",
                             col_types = cols(.default = "c"),
                             show_col_types = FALSE)
    write_csv(exclusivity, "data/raw/fda_exclusivity.csv")
    cat("✓ FDA exclusivity saved:", nrow(exclusivity), "records\n")
  }
  
  # Clean up
  unlink(temp_zip)
  
}, error = function(e) {
  cat("⚠ FDA Orange Book download failed:", e$message, "\n")
})

# ============================================================================
# Phase 3: Create derived datasets for Chapter 11
# ============================================================================

# Generic entry timing analysis
if (file.exists("data/raw/fda_products.csv") && 
    file.exists("data/raw/fda_exclusivity.csv")) {
  
  products <- read_csv("data/raw/fda_products.csv", show_col_types = FALSE)
  exclusivity <- read_csv("data/raw/fda_exclusivity.csv", show_col_types = FALSE)
  
  # Identify brand vs generic drugs
  entry_timing <- products %>%
    filter(!is.na(Appl_No)) %>%
    mutate(
      is_generic = Type == "ANDA",
      approval_date = as.Date(Approval_Date, format = "%b %d, %Y")
    ) %>%
    group_by(Ingredient, DF_Route) %>%
    arrange(approval_date) %>%
    mutate(
      first_approval = min(approval_date, na.rm = TRUE),
      first_generic = min(approval_date[is_generic], na.rm = TRUE),
      entry_lag_years = as.numeric(difftime(first_generic, first_approval, units = "days")) / 365.25
    ) %>%
    ungroup() %>%
    filter(!is.na(entry_lag_years), entry_lag_years >= 0) %>%
    distinct(Ingredient, DF_Route, .keep_all = TRUE)
  
  write_csv(entry_timing, "data/derived/generic_entry_timing.csv")
  cat("✓ Generic entry timing dataset created:", nrow(entry_timing), "drugs\n")
}

# ============================================================================
# Metadata
# ============================================================================

metadata <- tibble(
  dataset = c("patents_pharma", "patents_tech", "fda_products", 
              "fda_patents", "fda_exclusivity", "generic_entry_timing"),
  source = c("PatentsView API", "PatentsView API", "FDA Orange Book",
             "FDA Orange Book", "FDA Orange Book", "Derived from FDA"),
  chapter_use = c("Ch11", "Ch09, Ch11", "Ch11", "Ch11", "Ch11", "Ch11"),
  status = c(
    ifelse(file.exists("data/raw/patents_pharma.csv"), "Downloaded", "API call failed"),
    ifelse(file.exists("data/raw/patents_tech.csv"), "Downloaded", "API call failed"),
    ifelse(file.exists("data/raw/fda_products.csv"), "Downloaded", "Download failed"),
    ifelse(file.exists("data/raw/fda_patents.csv"), "Downloaded", "Download failed"),
    ifelse(file.exists("data/raw/fda_exclusivity.csv"), "Downloaded", "Download failed"),
    ifelse(file.exists("data/derived/generic_entry_timing.csv"), "Created", "Pending")
  ),
  notes = c(
    "Pharma patents 2010-present (CPC: A61K, A61P, C07D)",
    "Tech/software patents 2010-present (CPC: G06F, G06Q, H04L)",
    "FDA approved drug products",
    "Patent linkage data",
    "Market exclusivity periods",
    "Time from brand approval to first generic entry"
  ),
  date_created = Sys.Date()
)

write_csv(metadata, "data/raw/patents_fda_metadata.csv")

cat("\n✓ Patent & FDA data collection complete\n")

