# Extended FRED data pulls for antitrust book
# Chapters: 01-04 (orientation, research design, market definition, IO toolkit)
# Author: Automated data collection script
# Date: 2025-11-24

library(fredr)
library(dplyr)
library(tidyr)
library(readr)

# Set API key from environment
fredr_set_key(Sys.getenv("FRED_API_KEY"))

# ============================================================================
# Phase 1: Industry concentration & market power indicators
# ============================================================================

# Bank concentration (already used in Ch01)
bank_hhi <- fredr(series_id = "HHMSDODNS", 
                  observation_start = as.Date("2000-01-01"))

# Retail trade concentration
retail_hhi <- fredr(series_id = "DDOI06USA156NWDB",  # Retail trade HHI
                    observation_start = as.Date("2000-01-01"))

# Manufacturing concentration  
mfg_hhi <- fredr(series_id = "DDOI02USA156NWDB",  # Manufacturing HHI
                 observation_start = as.Date("2000-01-01"))

# ============================================================================
# Phase 2: Price series for cartel screens & pass-through
# ============================================================================

# Gasoline (already used)
gas_prices <- fredr(series_id = "GASREGW",
                    observation_start = as.Date("2000-01-01"))

# Crude oil (input for pass-through analysis)
crude_oil <- fredr(series_id = "DCOILWTICO",
                   observation_start = as.Date("2000-01-01"))

# Bread & bakery products (cartel example)
bread_cpi <- fredr(series_id = "CUSR0000SAF112",
                   observation_start = as.Date("2000-01-01"))

# Wheat (input for bread cartel)
wheat_price <- fredr(series_id = "PWHEAMTUSDM",
                     observation_start = as.Date("2000-01-01"))

# Steel products (cartel screens)
steel_ppi <- fredr(series_id = "PCU331331",
                   observation_start = as.Date("2000-01-01"))

# Cement (cartel example)
cement_ppi <- fredr(series_id = "PCU327310327310",
                    observation_start = as.Date("2000-01-01"))

# ============================================================================
# Phase 3: Labor market indicators (for Chapter 10)
# ============================================================================

# Average hourly earnings - all private
wages_all <- fredr(series_id = "CES0500000003",
                   observation_start = as.Date("2000-01-01"))

# Labor force participation rate
lfpr <- fredr(series_id = "CIVPART",
              observation_start = as.Date("2000-01-01"))

# Job openings rate
jolts <- fredr(series_id = "JTSJOR",
               observation_start = as.Date("2000-01-01"))

# ============================================================================
# Phase 4: Inflation & cost indices (for pass-through & IO models)
# ============================================================================

# CPI All items
cpi_all <- fredr(series_id = "CPIAUCSL",
                 observation_start = as.Date("2000-01-01"))

# PPI Final demand
ppi_final <- fredr(series_id = "PPIFIS",
                   observation_start = as.Date("2000-01-01"))

# Import price index
import_prices <- fredr(series_id = "IR",
                       observation_start = as.Date("2000-01-01"))

# ============================================================================
# Combine and save
# ============================================================================

# Create a master list
fred_data <- list(
  bank_hhi = bank_hhi,
  retail_hhi = retail_hhi,
  mfg_hhi = mfg_hhi,
  gas_prices = gas_prices,
  crude_oil = crude_oil,
  bread_cpi = bread_cpi,
  wheat_price = wheat_price,
  steel_ppi = steel_ppi,
  cement_ppi = cement_ppi,
  wages_all = wages_all,
  lfpr = lfpr,
  jolts = jolts,
  cpi_all = cpi_all,
  ppi_final = ppi_final,
  import_prices = import_prices
)

# Save individual series
for (name in names(fred_data)) {
  write_csv(fred_data[[name]], 
            file.path("data", "raw", paste0("fred_", name, ".csv")))
}

# Create a combined long-format dataset
fred_combined <- bind_rows(fred_data, .id = "series_name") %>%
  select(series_name, series_id, date, value)

write_csv(fred_combined, "data/raw/fred_combined.csv")

# Create metadata file
metadata <- tibble(
  series_name = names(fred_data),
  series_id = sapply(fred_data, function(x) unique(x$series_id)),
  description = c(
    "Bank deposits HHI",
    "Retail trade HHI",
    "Manufacturing HHI", 
    "Regular gasoline retail price",
    "WTI crude oil spot price",
    "CPI: Bread and bakery products",
    "Wheat price (monthly)",
    "PPI: Steel products",
    "PPI: Cement",
    "Average hourly earnings - all private",
    "Labor force participation rate",
    "Job openings rate",
    "CPI: All items",
    "PPI: Final demand",
    "Import price index"
  ),
  chapter_use = c(
    "Ch01, Ch03",
    "Ch03, Ch04",
    "Ch03, Ch04",
    "Ch01, Ch02, Ch05",
    "Ch04, Ch05",
    "Ch05",
    "Ch04, Ch05",
    "Ch05",
    "Ch05",
    "Ch10",
    "Ch10",
    "Ch10",
    "Ch04, Ch05",
    "Ch04, Ch05",
    "Ch04"
  ),
  date_pulled = Sys.Date()
)

write_csv(metadata, "data/raw/fred_metadata.csv")

cat("✓ FRED data collection complete\n")
cat("  - Series pulled:", length(fred_data), "\n")
cat("  - Files saved to: data/raw/\n")

