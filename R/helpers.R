# Shared helpers for reproducible figures and simple simulations.

library(ggplot2)

#' Antitrust book theme with PDF-friendly settings
#' 
#' Larger text sizes and cleaner legend positioning for readable PDF output.
#' Use with ggplot2: + theme_antitrust()
theme_antitrust <- function(base_size = 14) {
  theme_minimal(base_size = base_size) +
    theme(
      # Title and text sizing for PDF clarity
      plot.title = element_text(size = rel(1.2), face = "bold", margin = margin(b = 10)),
      plot.subtitle = element_text(size = rel(0.9), color = "gray40", margin = margin(b = 15)),
      plot.title.position = "plot",
      plot.caption = element_text(size = rel(0.7), color = "gray50", hjust = 0),
      
      # Axis text larger for PDF legibility
      axis.title = element_text(size = rel(0.9), face = "bold"),
      axis.text = element_text(size = rel(0.85)),
      axis.title.y = element_text(margin = margin(r = 10)),
      axis.title.x = element_text(margin = margin(t = 10)),
      
      # Legend: bottom placement prevents overlap with plot area
      legend.position = "bottom",
      legend.box = "horizontal",
      legend.title = element_text(size = rel(0.85), face = "bold"),
      legend.text = element_text(size = rel(0.8)),
      legend.key.size = unit(0.8, "lines"),
      legend.margin = margin(t = 10),
      legend.spacing.x = unit(0.5, "cm"),
      
      # Clean grid
      panel.grid.minor = element_blank(),
      panel.grid.major.x = element_line(color = "#e0e0e0", linewidth = 0.3),
      panel.grid.major.y = element_line(color = "#e0e0e0", linewidth = 0.3),
      
      # Add some padding
      plot.margin = margin(15, 15, 15, 15)
    )
}

#' Simplified theme variant for busy plots
#' 
#' More minimal styling when plots have many elements
theme_antitrust_minimal <- function(base_size = 14) {
  theme_antitrust(base_size) +
    theme(
      panel.grid.major.x = element_blank(),
      legend.position = "bottom",
      legend.direction = "horizontal"
    )
}

#' Color palette for antitrust figures
#' 
#' Colorblind-friendly palette with good contrast for PDF
antitrust_colors <- c(

  "blue"   = "#0072B2",
  "orange" = "#E69F00",
  "green"  = "#009E73",
  "red"    = "#D55E00",
  "purple" = "#CC79A7",
  "cyan"   = "#56B4E9",
  "gray"   = "#999999"
)

#' Scale for discrete colors
scale_color_antitrust <- function(...) {

  scale_color_manual(values = unname(antitrust_colors), ...)
}

#' Scale for fills
scale_fill_antitrust <- function(...) {
  scale_fill_manual(values = unname(antitrust_colors), ...)
}

# Quick FRED pull with caching to data/raw.
fetch_fred <- function(series_id, start = as.Date("1990-01-01")) {
  if (!requireNamespace("fredr", quietly = TRUE)) {
    stop("Install fredr to fetch FRED series.")
  }
  fredr::fredr_set_key(Sys.getenv("FRED_API_KEY"))
  fredr::fredr(series_id = series_id, observation_start = start)
}

# Simple differentiated products logit simulation (static, no nests) for teaching.
# products: data.frame with columns product, firm, price, share, mc (or margin)
run_logit_sim <- function(products, merging_firms) {
  stopifnot(all(c("product", "firm", "price", "share") %in% names(products)))
  if (!"mc" %in% names(products)) {
    stop("Provide marginal costs in column `mc` (or add price * (1 - margin)).")
  }

  # implied mean utility up to constant (outside share from 1 - sum shares)
  s0 <- 1 - sum(products$share)
  if (s0 <= 0) stop("Outside share must be positive.")
  products$delta <- log(products$share) - log(s0)

  # calibrate alpha using price coefficient from simple regression
  fit <- lm(delta ~ price, data = products)
  alpha <- -abs(coef(fit)[["price"]])

  # post-merger ownership matrix
  firms_post <- products$firm
  firms_post[products$firm %in% merging_firms] <- paste(merging_firms, collapse = "+")
  own <- outer(firms_post, firms_post, "==")

  # first-order condition: p = mc + (1/-alpha) * inv(share matrix) * share
  shares <- products$share
  jac <- -alpha * (diag(shares) - shares %o% shares)
  foc_mat <- own * jac
  price_change <- solve(foc_mat, shares)
  new_prices <- products$mc + price_change

  list(
    alpha = alpha,
    prices_pre = products$price,
    prices_post = as.numeric(new_prices),
    delta = products$delta,
    ownership_post = firms_post
  )
}
