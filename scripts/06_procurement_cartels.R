# Procurement and cartel screening data
# World Bank procurement + synthetic cartel examples
# Author: Automated data collection script
# Date: 2025-11-24

library(dplyr)
library(tidyr)
library(readr)
library(httr)
library(jsonlite)

# ============================================================================
# Phase 1: World Bank procurement data
# ============================================================================

# World Bank Major Contract Awards
# API: https://finances.worldbank.org/resource/kdui-wcs3.json

cat("Querying World Bank procurement data...\n")

wb_base_url <- "https://finances.worldbank.org/resource/kdui-wcs3.json"

# Query with filters for recent years and relevant sectors
wb_query <- paste0(wb_base_url, "?$limit=50000&$where=fiscal_year>='2015'")

tryCatch({
  response <- GET(wb_query)
  
  if (status_code(response) == 200) {
    wb_data <- content(response, as = "parsed") %>%
      bind_rows() %>%
      as_tibble()
    
    # Clean and standardize
    wb_clean <- wb_data %>%
      mutate(
        contract_amount = as.numeric(total_contract_amount),
        fiscal_year = as.integer(fiscal_year)
      ) %>%
      filter(!is.na(contract_amount), contract_amount > 0)
    
    write_csv(wb_clean, "data/raw/worldbank_procurement.csv")
    cat("✓ World Bank procurement data saved:", nrow(wb_clean), "contracts\n")
  } else {
    cat("⚠ World Bank API returned status:", status_code(response), "\n")
  }
}, error = function(e) {
  cat("⚠ World Bank API call failed:", e$message, "\n")
})

# ============================================================================
# Phase 2: Create synthetic cartel screening datasets
# ============================================================================

# Based on literature examples (bread cartel, cement cartel, etc.)

set.seed(123)

# Example 1: Bread cartel (South Africa context)
# Simulate price series with structural break

dates <- seq(as.Date("2010-01-01"), as.Date("2023-12-01"), by = "month")
n_months <- length(dates)

# Cartel period: 2012-01 to 2016-12 (60 months)
cartel_start <- which(dates == as.Date("2012-01-01"))
cartel_end <- which(dates == as.Date("2016-12-01"))

bread_prices <- tibble(
  date = dates,
  # Base price with trend
  base_price = 15 + 0.02 * seq_along(dates) + rnorm(n_months, 0, 0.5),
  # Cartel markup
  cartel_markup = ifelse(seq_along(dates) >= cartel_start & 
                          seq_along(dates) <= cartel_end, 2.5, 0),
  # Observed price
  price = base_price + cartel_markup + rnorm(n_months, 0, 0.3),
  # Quantity (negatively correlated with price)
  quantity = 1000 - 15 * price + rnorm(n_months, 0, 50),
  product = "Bread (700g loaf)"
)

write_csv(bread_prices, "data/derived/cartel_bread_prices.csv")

# Example 2: Cement cartel - bid rotation pattern
n_projects <- 200
firms <- c("Firm_A", "Firm_B", "Firm_C", "Firm_D")

# Pre-cartel: competitive bidding (2010-2013)
# Cartel: rotation pattern (2014-2018)
# Post-cartel: return to competition (2019+)

cement_bids <- tibble(
  project_id = 1:n_projects,
  date = seq(as.Date("2010-01-01"), by = "month", length.out = n_projects),
  year = lubridate::year(date)
) %>%
  mutate(
    # Assign winner based on period
    cartel_period = year >= 2014 & year <= 2018,
    # During cartel: systematic rotation
    winner = if_else(
      cartel_period,
      firms[(project_id %% length(firms)) + 1],
      sample(firms, n(), replace = TRUE, prob = c(0.3, 0.25, 0.25, 0.2))
    ),
    # Bid amounts
    base_cost = rnorm(n(), 500000, 100000),
    markup = if_else(cartel_period, 
                     rnorm(n(), 0.25, 0.05),  # Higher markup during cartel
                     rnorm(n(), 0.10, 0.08)), # Competitive markup
    winning_bid = base_cost * (1 + markup)
  )

write_csv(cement_bids, "data/derived/cartel_cement_bids.csv")

# Example 3: Price correlation matrix (for variance screen)
# Simulate prices for multiple firms/products

firms_prices <- expand_grid(
  date = seq(as.Date("2015-01-01"), as.Date("2023-12-01"), by = "month"),
  firm = paste0("Firm_", LETTERS[1:5])
) %>%
  group_by(firm) %>%
  mutate(
    # Base price with common shock
    common_shock = rnorm(n(), 0, 2),
    # Firm-specific shock (larger during competition)
    firm_shock = rnorm(n(), 0, if_else(date < as.Date("2018-01-01"), 3, 0.5)),
    # Price
    price = 100 + common_shock + firm_shock + 0.01 * row_number()
  ) %>%
  ungroup()

write_csv(firms_prices, "data/derived/cartel_price_correlation.csv")

# ============================================================================
# Phase 3: Bid screening metrics
# ============================================================================

if (file.exists("data/derived/cartel_cement_bids.csv")) {
  bids <- read_csv("data/derived/cartel_cement_bids.csv", show_col_types = FALSE)
  
  # Calculate bid rotation metrics
  rotation_metrics <- bids %>%
    group_by(year, winner) %>%
    summarise(
      wins = n(),
      avg_bid = mean(winning_bid),
      .groups = "drop"
    ) %>%
    group_by(year) %>%
    mutate(
      total_projects = sum(wins),
      win_share = wins / total_projects,
      # Rotation index: lower variance = more rotation
      rotation_index = sd(win_share)
    )
  
  write_csv(rotation_metrics, "data/derived/cartel_rotation_metrics.csv")
}

# ============================================================================
# Metadata
# ============================================================================

metadata <- tibble(
  dataset = c("worldbank_procurement", "bread_prices", "cement_bids", 
              "price_correlation", "rotation_metrics"),
  source = c("World Bank API", "Synthetic", "Synthetic", "Synthetic", "Derived"),
  chapter_use = c("Ch05", "Ch05", "Ch05", "Ch05", "Ch05"),
  description = c(
    "World Bank major contract awards 2015+",
    "Bread cartel price series with structural break",
    "Cement cartel bid rotation pattern",
    "Multi-firm price correlation for variance screen",
    "Bid rotation metrics by year and firm"
  ),
  status = c(
    ifelse(file.exists("data/raw/worldbank_procurement.csv"), "Downloaded", "API call failed"),
    "Synthetic",
    "Synthetic",
    "Synthetic",
    "Derived"
  ),
  notes = c(
    "Real procurement data for bid analysis",
    "Replace with Stats SA CPI or actual bread prices",
    "Replace with actual bid data from competition authority",
    "Demonstrates variance screen methodology",
    "Rotation index: lower = more systematic rotation"
  ),
  date_created = Sys.Date()
)

write_csv(metadata, "data/raw/procurement_cartels_metadata.csv")

cat("\n✓ Procurement & cartel data collection complete\n")

