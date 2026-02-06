# BLS labor market data for Chapter 10 (labor markets)
# County-level employment concentration (HHI)
# Author: Automated data collection script
# Date: 2025-11-24

library(dplyr)
library(tidyr)
library(readr)
library(httr)
library(jsonlite)
library(lubridate)

# Note: BLS QCEW API requires registration at https://data.bls.gov/registrationEngine/
# For now, we'll use the public bulk download approach

# ============================================================================
# Option 1: Use blscrapeR package for easier access
# ============================================================================

if (!requireNamespace("blscrapeR", quietly = TRUE)) {
  stop("Package 'blscrapeR' is required but not installed. ",
       "Install with: install.packages('blscrapeR')")
}
library(blscrapeR)

# ============================================================================
# Pull national employment data by industry (NAICS 2-digit)
# ============================================================================

# Series IDs for total nonfarm employment by major industry
# Format: CEU + supersector code + 00000001 (all employees, thousands)
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

# Pull data for last 15 years
start_year <- year(Sys.Date()) - 15
end_year <- year(Sys.Date())

employment_data <- lapply(industry_series, function(series) {
  tryCatch({
    bls_api(series, 
            startyear = start_year, 
            endyear = end_year,
            registrationKey = Sys.getenv("BLS_KEY"))
  }, error = function(e) {
    cat("Warning: Could not fetch", series, "\n")
    return(NULL)
  })
}) |>
  bind_rows()

if (nrow(employment_data) > 0) {
  write_csv(employment_data, "data/raw/bls_industry_employment.csv")
  cat("✓ BLS industry employment data saved\n")
} else {
  cat("⚠ BLS API call failed. Check BLS_KEY in .Renviron\n")
}

# ============================================================================
# Option 2: Download QCEW county-level data (bulk files)
# ============================================================================

# QCEW county-level data is available as quarterly CSV files
# URL pattern: https://data.bls.gov/cew/data/files/[year]/csv/[year]_qtrly_singlefile.zip

# For demonstration, we'll document the process and create a stub
qcew_note <- "
# BLS QCEW County-Level Data Collection

## Manual download steps:
1. Visit: https://www.bls.gov/cew/downloadable-data-files.htm
2. Download annual single-file CSVs for years 2010-2024
3. Extract to data/raw/qcew/
4. Run processing script to compute county-level HHIs

## Automated download (requires large storage):
wget https://data.bls.gov/cew/data/files/2023/csv/2023_qtrly_singlefile.zip
unzip 2023_qtrly_singlefile.zip -d data/raw/qcew/

## Key fields for HHI calculation:
- area_fips: County FIPS code
- own_code: Ownership (5 = private)
- industry_code: NAICS code
- qtr: Quarter
- annual_avg_emplvl: Average employment

## Processing steps:
1. Filter to private sector (own_code == 5)
2. Aggregate employment by county × industry
3. Compute market shares within county
4. Calculate HHI = sum(share^2) × 10,000
"

write_lines(qcew_note, "data/raw/bls_qcew_notes.txt")

# ============================================================================
# Option 3: Use OES (Occupational Employment Statistics) for wage data
# ============================================================================

# OES provides occupation-level wage data by area
# Useful for monopsony analysis in Chapter 10

oes_note <- "
# BLS OES (Occupational Employment and Wage Statistics)

## Data source:
https://www.bls.gov/oes/tables.htm

## Key files:
- National occupational employment and wage estimates
- State and metropolitan area estimates
- Industry-specific estimates

## Relevant for Chapter 10:
- Wage distributions by occupation and geography
- Employment concentration by occupation
- Wage posting analysis

## Download instructions:
1. Visit: https://www.bls.gov/oes/tables.htm
2. Download 'All data' Excel files for recent years
3. Extract occupation × area × wage data
4. Compute labor market concentration metrics

## Example series (via API):
- OEUM000000000000003: Mean hourly wage, all occupations
- OEUM000000000000004: Median hourly wage, all occupations
"

write_lines(oes_note, "data/raw/bls_oes_notes.txt")

# ============================================================================
# Create a synthetic county-level HHI dataset for demonstration
# (Replace with real QCEW data when available)
# ============================================================================

set.seed(123)
counties <- c("Los Angeles, CA", "Cook, IL", "Harris, TX", "Maricopa, AZ", 
              "San Diego, CA", "Orange, CA", "Miami-Dade, FL", "Kings, NY",
              "Dallas, TX", "Queens, NY")

years <- 2015:2023

synthetic_hhi <- expand_grid(
  county = counties,
  year = years
) |>
  mutate(
    # Simulate HHI with some variation
    hhi_retail = rnorm(n(), mean = 1200, sd = 300),
    hhi_healthcare = rnorm(n(), mean = 1800, sd = 400),
    hhi_hospitality = rnorm(n(), mean = 900, sd = 200),
    hhi_manufacturing = rnorm(n(), mean = 1500, sd = 350),
    # Ensure HHI bounds (clamp to 500-10000 range)
    across(starts_with("hhi_"), \(x) pmax(500, pmin(10000, x)))
  )

write_csv(synthetic_hhi, "data/derived/labor_market_hhi_synthetic.csv")

# ============================================================================
# Metadata
# ============================================================================

metadata <- tibble(
  dataset = c("industry_employment", "qcew_county", "oes_wages", "synthetic_hhi"),
  source = c("BLS CES API", "BLS QCEW bulk download", "BLS OES tables", "Synthetic"),
  chapter_use = c("Ch10", "Ch10", "Ch10", "Ch10"),
  status = c(
    ifelse(exists("employment_data") && nrow(employment_data) > 0, "Downloaded", "Pending API key"),
    "Manual download required",
    "Manual download required",
    "Synthetic placeholder"
  ),
  notes = c(
    "National employment by industry",
    "County-level employment for HHI calculation",
    "Occupation-level wages by area",
    "Replace with real QCEW data"
  ),
  date_created = Sys.Date()
)

write_csv(metadata, "data/raw/bls_metadata.csv")

cat("✓ BLS labor market data collection setup complete\n")
cat("  - Industry employment:", ifelse(exists("employment_data"), "✓", "⚠ API key needed"), "\n")
cat("  - County QCEW: ⚠ Manual download required\n")
cat("  - Synthetic HHI: ✓ Created for demonstration\n")

