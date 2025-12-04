# Install missing packages for data collection
# Author: Automated setup
# Date: 2025-11-24

# Set CRAN mirror
options(repos = c(CRAN = "https://cloud.r-project.org/"))

# List of required packages
required_packages <- c(
  "fredr",
  "tidyquant",
  "dplyr",
  "tidyr",
  "readr",
  "httr",
  "jsonlite",
  "lubridate",
  "nycflights13",
  "ggplot2",
  "tibble",
  "purrr"
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

cat("\n✓ Package installation complete!\n")

