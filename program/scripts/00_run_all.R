# Master script to run all data collection scripts
# Author: Automated data collection
# Date: 2025-11-24

cat("========================================\n")
cat("Antitrust Book Data Collection Pipeline\n")
cat("========================================\n\n")

# Check for required packages
required_packages <- c(
  "fredr", "tidyquant", "dplyr", "tidyr", "readr", "httr", "jsonlite",
  "lubridate", "nycflights13"
)

missing_packages <- required_packages[!sapply(required_packages, requireNamespace, quietly = TRUE)]

if (length(missing_packages) > 0) {
  cat("⚠ Missing packages:", paste(missing_packages, collapse = ", "), "\n")
  cat("Install with: install.packages(c('", paste(missing_packages, collapse = "', '"), "'))\n\n")
}

# Check for API keys
api_keys <- c("FRED_API_KEY", "BLS_KEY")
missing_keys <- api_keys[Sys.getenv(api_keys) == ""]

if (length(missing_keys) > 0) {
  cat("⚠ Missing API keys:", paste(missing_keys, collapse = ", "), "\n")
  cat("  Add to .Renviron file (copy from .Renviron.example)\n")
  cat("  FRED API key: https://fred.stlouisfed.org/docs/api/api_key.html\n")
  cat("  BLS API key: https://www.bls.gov/developers/home.htm\n\n")
}

# Create directory structure
if (!dir.exists("data/raw")) dir.create("data/raw", recursive = TRUE)
if (!dir.exists("data/derived")) dir.create("data/derived", recursive = TRUE)

cat("Starting data collection...\n\n")

# ============================================================================
# Script 01: FRED extended data
# ============================================================================
cat("01. FRED extended data (concentration, prices, labor)...\n")
tryCatch({
  source("program/scripts/01_fred_extended.R")
}, error = function(e) {
  cat("   ⚠ Error:", e$message, "\n")
})
cat("\n")

# ============================================================================
# Script 02: Financial data extended
# ============================================================================
cat("02. Financial data (event studies)...\n")
tryCatch({
  source("program/scripts/02_finance_extended.R")
}, error = function(e) {
  cat("   ⚠ Error:", e$message, "\n")
})
cat("\n")

# ============================================================================
# Script 03: BLS labor market data
# ============================================================================
cat("03. BLS labor market data...\n")
tryCatch({
  source("program/scripts/03_bls_labor.R")
}, error = function(e) {
  cat("   ⚠ Error:", e$message, "\n")
})
cat("\n")

# ============================================================================
# Script 04: Patents and FDA data
# ============================================================================
cat("04. Patents (PatentsView) and FDA Orange Book...\n")
tryCatch({
  source("program/scripts/04_patents_fda.R")
}, error = function(e) {
  cat("   ⚠ Error:", e$message, "\n")
})
cat("\n")

# ============================================================================
# Script 05: Flights extended
# ============================================================================
cat("05. Airline/flights data (nycflights13)...\n")
tryCatch({
  source("program/scripts/05_flights_extended.R")
}, error = function(e) {
  cat("   ⚠ Error:", e$message, "\n")
})
cat("\n")

# ============================================================================
# Script 06: Procurement and cartels
# ============================================================================
cat("06. Procurement and cartel screening data...\n")
tryCatch({
  source("program/scripts/06_procurement_cartels.R")
}, error = function(e) {
  cat("   ⚠ Error:", e$message, "\n")
})
cat("\n")

# ============================================================================
# Script 07: Digital platforms
# ============================================================================
cat("07. Digital platforms data...\n")
tryCatch({
  source("program/scripts/07_digital_platforms.R")
}, error = function(e) {
  cat("   ⚠ Error:", e$message, "\n")
})
cat("\n")

# ============================================================================
# Script 08: Regulation and benchmarks
# ============================================================================
cat("08. Regulation and benchmarking data...\n")
tryCatch({
  source("program/scripts/08_regulation_benchmarks.R")
}, error = function(e) {
  cat("   ⚠ Error:", e$message, "\n")
})
cat("\n")

# ============================================================================
# Summary
# ============================================================================
cat("========================================\n")
cat("Data Collection Summary\n")
cat("========================================\n\n")

# Count files in raw and derived
raw_files <- list.files("data/raw", pattern = "\\.csv$")
derived_files <- list.files("data/derived", pattern = "\\.csv$")

cat("Files created:\n")
cat("  - data/raw:", length(raw_files), "files\n")
cat("  - data/derived:", length(derived_files), "files\n\n")

cat("Next steps:\n")
cat("1. Review metadata files in data/raw/ and data/derived/\n")
cat("2. Update chapter code chunks to read from data/derived/\n")
cat("3. Set cache: true for API-dependent chunks\n")
cat("4. Document data provenance in chapters/13-empirical-appendix.qmd\n")
cat("5. Update data/README.md with new datasets\n\n")

cat("✓ Data collection pipeline complete!\n")

