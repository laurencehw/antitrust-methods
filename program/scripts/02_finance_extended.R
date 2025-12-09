# Extended financial data pulls for antitrust book
# Event studies for mergers, monopolization, digital markets
# Author: Automated data collection script
# Date: 2025-11-24

library(tidyquant)
library(dplyr)
library(tidyr)
library(readr)
library(lubridate)

# ============================================================================
# Phase 1: Airline mergers (already used in Ch02, Ch06)
# ============================================================================

airline_tickers <- c("AAL", "DAL", "LUV", "UAL", "JBLU", "ALK", "SPY")
airline_start <- as.Date("2010-01-01")
airline_end <- Sys.Date()

airlines <- tq_get(
  airline_tickers,
  from = airline_start,
  to = airline_end,
  get = "stock.prices"
)

write_csv(airlines, "data/raw/finance_airlines.csv")

# ============================================================================
# Phase 2: Tech platforms (for Ch09 - digital markets)
# ============================================================================

tech_tickers <- c("GOOGL", "META", "AMZN", "AAPL", "MSFT", "NFLX", "SPY")
tech_start <- as.Date("2010-01-01")
tech_end <- Sys.Date()

tech_platforms <- tq_get(
  tech_tickers,
  from = tech_start,
  to = tech_end,
  get = "stock.prices"
)

write_csv(tech_platforms, "data/raw/finance_tech_platforms.csv")

# ============================================================================
# Phase 3: Healthcare/Pharma (for Ch06, Ch11)
# ============================================================================

health_tickers <- c("UNH", "CVS", "CI", "ANTM", "HUM",  # Insurers
                    "PFE", "JNJ", "MRK", "ABBV", "LLY",  # Pharma
                    "HCA", "THC", "CYH",  # Hospital chains
                    "SPY")
health_start <- as.Date("2010-01-01")
health_end <- Sys.Date()

healthcare <- tq_get(
  health_tickers,
  from = health_start,
  to = health_end,
  get = "stock.prices"
)

write_csv(healthcare, "data/raw/finance_healthcare.csv")

# ============================================================================
# Phase 4: Telecom (for Ch08 - regulation)
# ============================================================================

telecom_tickers <- c("T", "VZ", "TMUS", "CHTR", "CMCSA", "SPY")
telecom_start <- as.Date("2010-01-01")
telecom_end <- Sys.Date()

telecom <- tq_get(
  telecom_tickers,
  from = telecom_start,
  to = telecom_end,
  get = "stock.prices"
)

write_csv(telecom, "data/raw/finance_telecom.csv")

# ============================================================================
# Phase 5: Retail (for Ch03, Ch05, Ch06)
# ============================================================================

retail_tickers <- c("WMT", "TGT", "COST", "KR", "ACI",  # Grocery/big box
                    "AMZN",  # E-commerce
                    "SPY")
retail_start <- as.Date("2010-01-01")
retail_end <- Sys.Date()

retail <- tq_get(
  retail_tickers,
  from = retail_start,
  to = retail_end,
  get = "stock.prices"
)

write_csv(retail, "data/raw/finance_retail.csv")

# ============================================================================
# Create metadata
# ============================================================================

metadata <- tibble(
  dataset = c("airlines", "tech_platforms", "healthcare", "telecom", "retail"),
  tickers = c(
    paste(airline_tickers, collapse = ", "),
    paste(tech_tickers, collapse = ", "),
    paste(health_tickers, collapse = ", "),
    paste(telecom_tickers, collapse = ", "),
    paste(retail_tickers, collapse = ", ")
  ),
  chapter_use = c(
    "Ch02, Ch06",
    "Ch09",
    "Ch06, Ch11",
    "Ch08",
    "Ch03, Ch05, Ch06"
  ),
  date_range = paste(airline_start, "to", Sys.Date()),
  date_pulled = Sys.Date(),
  notes = c(
    "Merger event studies (AA/US Airways, etc.)",
    "Platform competition, antitrust investigations",
    "Hospital/pharma mergers, pay-for-delay",
    "Merger reviews, regulatory changes",
    "Market definition, cartel screens, merger retrospectives"
  )
)

write_csv(metadata, "data/raw/finance_metadata.csv")

cat("✓ Financial data collection complete\n")
cat("  - Datasets:", nrow(metadata), "\n")
cat("  - Files saved to: data/raw/\n")

