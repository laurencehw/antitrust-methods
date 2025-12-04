# Extended airline/flights data for market definition & merger analysis
# Using nycflights13 + additional route/carrier metrics
# Author: Automated data collection script
# Date: 2025-11-24

library(nycflights13)
library(dplyr)
library(tidyr)
library(readr)

# ============================================================================
# Phase 1: Route-level market shares (already used in Ch03)
# ============================================================================

# Calculate route shares from nycflights13
route_shares <- flights %>%
  filter(!is.na(origin), !is.na(dest)) %>%
  mutate(route = paste(pmin(origin, dest), pmax(origin, dest), sep = "-")) %>%
  group_by(route, carrier) %>%
  summarise(
    flights = n(),
    avg_distance = mean(distance, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  group_by(route) %>%
  mutate(
    total_flights = sum(flights),
    share = flights / total_flights,
    hhi = sum(share^2) * 10000
  ) %>%
  ungroup()

write_csv(route_shares, "data/derived/airline_route_shares.csv")

# ============================================================================
# Phase 2: Hub concentration metrics
# ============================================================================

hub_concentration <- flights %>%
  filter(!is.na(origin), !is.na(carrier)) %>%
  group_by(origin, carrier) %>%
  summarise(
    flights = n(),
    destinations = n_distinct(dest),
    .groups = "drop"
  ) %>%
  group_by(origin) %>%
  mutate(
    total_flights = sum(flights),
    share = flights / total_flights,
    hhi = sum(share^2) * 10000
  ) %>%
  arrange(origin, desc(share))

write_csv(hub_concentration, "data/derived/airline_hub_concentration.csv")

# ============================================================================
# Phase 3: Carrier-level metrics
# ============================================================================

carrier_metrics <- flights %>%
  left_join(nycflights13::airlines, by = "carrier") %>%
  group_by(carrier, name) %>%
  summarise(
    total_flights = n(),
    routes = n_distinct(paste(origin, dest, sep = "-")),
    airports = n_distinct(c(origin, dest)),
    avg_distance = mean(distance, na.rm = TRUE),
    avg_delay = mean(arr_delay, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  arrange(desc(total_flights))

write_csv(carrier_metrics, "data/derived/airline_carrier_metrics.csv")

# ============================================================================
# Phase 4: Time-of-day patterns (for capacity/slot analysis)
# ============================================================================

hourly_patterns <- flights %>%
  filter(!is.na(hour)) %>%
  group_by(origin, hour, carrier) %>%
  summarise(
    flights = n(),
    .groups = "drop"
  ) %>%
  group_by(origin, hour) %>%
  mutate(
    total_flights = sum(flights),
    share = flights / total_flights
  )

write_csv(hourly_patterns, "data/derived/airline_hourly_patterns.csv")

# ============================================================================
# Phase 5: Delay analysis (quality dimension for market definition)
# ============================================================================

delay_analysis <- flights %>%
  filter(!is.na(arr_delay)) %>%
  mutate(
    route = paste(pmin(origin, dest), pmax(origin, dest), sep = "-"),
    delayed = arr_delay > 15
  ) %>%
  group_by(route, carrier) %>%
  summarise(
    flights = n(),
    avg_delay = mean(arr_delay, na.rm = TRUE),
    pct_delayed = mean(delayed, na.rm = TRUE) * 100,
    .groups = "drop"
  )

write_csv(delay_analysis, "data/derived/airline_delay_analysis.csv")

# ============================================================================
# Metadata
# ============================================================================

metadata <- tibble(
  dataset = c("route_shares", "hub_concentration", "carrier_metrics", 
              "hourly_patterns", "delay_analysis"),
  source = "nycflights13 package",
  chapter_use = c("Ch03, Ch06", "Ch03, Ch06", "Ch03, Ch06", "Ch06, Ch07", "Ch03"),
  description = c(
    "Market shares by route and carrier",
    "Hub concentration (HHI) by airport",
    "Carrier-level summary statistics",
    "Hourly flight patterns by airport and carrier",
    "Delay metrics by route and carrier"
  ),
  rows = c(
    nrow(route_shares),
    nrow(hub_concentration),
    nrow(carrier_metrics),
    nrow(hourly_patterns),
    nrow(delay_analysis)
  ),
  date_created = Sys.Date()
)

write_csv(metadata, "data/derived/flights_metadata.csv")

cat("✓ Airline/flights data processing complete\n")
cat("  - Route shares:", nrow(route_shares), "route-carrier pairs\n")
cat("  - Hub concentration:", length(unique(hub_concentration$origin)), "airports\n")
cat("  - Carrier metrics:", nrow(carrier_metrics), "carriers\n")

