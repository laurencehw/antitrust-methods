# Shared helpers for reproducible figures and simple simulations.

library(ggplot2)

theme_antitrust <- function() {
  theme_minimal(base_size = 12) +
    theme(
      plot.title.position = "plot",
      panel.grid.minor = element_blank(),
      panel.grid.major.x = element_line(color = "#e9e9e9"),
      panel.grid.major.y = element_line(color = "#e9e9e9")
    )
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
