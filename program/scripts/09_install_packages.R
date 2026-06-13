# Install missing packages for data collection
# Author: Automated setup
# Date: 2025-11-24

# Set CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org/"))

# Every package loaded by a chapter chunk, helpers.R, or a pipeline script.
# Keep this list in sync when adding a library() call anywhere in the book.
required_packages <- c(
  # Core tidyverse + plotting
  "dplyr", "tidyr", "readr", "tibble", "purrr", "stringr", "forcats",
  "magrittr", "ggplot2", "scales", "viridis", "patchwork", "knitr",
  # Data access
  "fredr", "tidyquant", "httr", "jsonlite", "censusapi", "blsAPI",
  "blscrapeR", "nycflights13",
  # Dates and panels
  "lubridate", "zoo",
  # Econometrics and ML
  "fixest", "did", "Synth", "strucchange", "survival", "survminer",
  "survey", "ranger", "pwr",
  # Graphs and maps
  "igraph", "ggraph", "maps"
)

cat("Installing missing packages...\n\n")

for (pkg in required_packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    cat("Installing", pkg, "...\n")
    install.packages(pkg, quiet = TRUE)
  } else {
    cat("✓", pkg, "already installed\n")
  }
}

# ggsankey is not on CRAN; install from GitHub
if (!requireNamespace("ggsankey", quietly = TRUE)) {
  if (!requireNamespace("remotes", quietly = TRUE)) {
    install.packages("remotes", quiet = TRUE)
  }
  cat("Installing ggsankey from GitHub (davidsjoberg/ggsankey)...\n")
  remotes::install_github("davidsjoberg/ggsankey", quiet = TRUE)
} else {
  cat("✓ ggsankey already installed\n")
}

cat("\n✓ Package installation complete!\n")

