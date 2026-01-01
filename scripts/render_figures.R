# Render all figures from Quarto chapters for GitBook
# This script extracts R code chunks that produce figures and renders them as PNGs

library(knitr)
library(ggplot2)

# Set working directory to project root
# Get script location from command args or use current directory
args <- commandArgs(trailingOnly = FALSE)
script_path <- sub("--file=", "", args[grep("--file=", args)])
if (length(script_path) > 0) {
  project_root <- normalizePath(file.path(dirname(script_path), ".."))
} else {
  project_root <- getwd()
}
setwd(project_root)
message(sprintf("Project root: %s", project_root))

# Source helpers
source("program/R/helpers.R")

# Output directory for figures
fig_dir <- file.path(project_root, "gitbook", "figures")
dir.create(fig_dir, showWarnings = FALSE, recursive = TRUE)

# Function to extract and run figure chunks from a .qmd file
render_chapter_figures <- function(qmd_file, chapter_name) {
  message(sprintf("Processing: %s", basename(qmd_file)))

  # Read the file
  content <- readLines(qmd_file, warn = FALSE)
  content <- paste(content, collapse = "\n")

  # Find all R code chunks
  chunk_pattern <- "```\\{r\\}[^`]*```"
  chunks <- gregexpr(chunk_pattern, content, perl = TRUE)

  if (chunks[[1]][1] == -1) {
    message("  No R chunks found")
    return(NULL)
  }

  # Extract chunk contents
  matches <- regmatches(content, chunks)[[1]]

  figures_created <- character(0)
  fig_num <- 0

  for (i in seq_along(matches)) {
    chunk <- matches[i]

    # Remove fence markers
    code <- sub("^```\\{r\\}\n?", "", chunk)
    code <- sub("\n?```$", "", code)

    # Remove chunk options (lines starting with #|)
    code_lines <- strsplit(code, "\n")[[1]]
    code_lines <- code_lines[!grepl("^#\\|", code_lines)]
    code <- paste(code_lines, collapse = "\n")

    # Skip empty chunks or chunks with eval: false
    if (nchar(trimws(code)) == 0) next
    if (grepl("eval:\\s*false", chunk)) next

    # Check if this chunk likely produces a figure (contains ggplot, plot, etc.)
    if (!grepl("ggplot|plot\\(|geom_|hist\\(|barplot|boxplot", code, ignore.case = TRUE)) {
      next
    }

    fig_num <- fig_num + 1
    fig_filename <- sprintf("%s_fig%02d.png", chapter_name, fig_num)
    fig_path <- file.path(fig_dir, fig_filename)

    # Try to execute and save
    tryCatch({
      # Open PNG device
      png(fig_path, width = 8, height = 5, units = "in", res = 150)

      # Execute the code
      result <- eval(parse(text = code))

      # If result is a ggplot, print it
      if (inherits(result, "ggplot") || inherits(result, "gg")) {
        print(result)
      }

      dev.off()

      # Check if file was created and has content
      if (file.exists(fig_path) && file.info(fig_path)$size > 1000) {
        message(sprintf("  Created: %s", fig_filename))
        figures_created <- c(figures_created, fig_filename)
      } else {
        # Remove empty/failed files
        if (file.exists(fig_path)) file.remove(fig_path)
      }
    }, error = function(e) {
      message(sprintf("  Error in chunk %d: %s", i, conditionMessage(e)))
      if (dev.cur() > 1) dev.off()
      if (file.exists(fig_path)) file.remove(fig_path)
    })
  }

  return(figures_created)
}

# Get all chapter files
chapter_files <- list.files(
  file.path(project_root, "chapters"),
  pattern = "\\.qmd$",
  full.names = TRUE
)

# Also include index.qmd if it exists
index_file <- file.path(project_root, "index.qmd")
if (file.exists(index_file)) {
  chapter_files <- c(index_file, chapter_files)
}

# Render figures for each chapter
all_figures <- list()

for (qmd_file in chapter_files) {
  chapter_name <- tools::file_path_sans_ext(basename(qmd_file))
  figs <- render_chapter_figures(qmd_file, chapter_name)
  if (length(figs) > 0) {
    all_figures[[chapter_name]] <- figs
  }
}

# Summary
message("\n=== Summary ===")
total_figs <- sum(sapply(all_figures, length))
message(sprintf("Total figures rendered: %d", total_figs))

for (chapter in names(all_figures)) {
  message(sprintf("  %s: %d figures", chapter, length(all_figures[[chapter]])))
}

# Save manifest
manifest <- data.frame(
  chapter = rep(names(all_figures), sapply(all_figures, length)),
  figure = unlist(all_figures),
  stringsAsFactors = FALSE
)
write.csv(manifest, file.path(fig_dir, "manifest.csv"), row.names = FALSE)
message(sprintf("\nManifest saved to: %s", file.path(fig_dir, "manifest.csv")))
