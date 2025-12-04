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

# Timeline visualization for remedy compliance, merger milestones, etc.
# events: data.frame with columns date, event, category (optional), description (optional)
plot_timeline <- function(events, title = "Event Timeline", date_breaks = "3 months") {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    stop("Install ggplot2 to create timeline plots.")
  }
  if (!all(c("date", "event") %in% names(events))) {
    stop("events must have columns 'date' and 'event'")
  }

  events$date <- as.Date(events$date)
  events$y_position <- seq_len(nrow(events)) %% 3

  p <- ggplot(events, aes(x = date, y = y_position)) +
    geom_segment(aes(xend = date, yend = 0), color = "#666666", linewidth = 0.5) +
    geom_point(size = 3, color = "#0072B2") +
    geom_text(aes(label = event), hjust = 0, nudge_x = 5, size = 3) +
    scale_x_date(date_breaks = date_breaks, date_labels = "%b %Y") +
    labs(title = title, x = "Date", y = NULL) +
    theme_antitrust() +
    theme(
      axis.text.y = element_blank(),
      axis.ticks.y = element_blank(),
      panel.grid.major.y = element_blank()
    )

  p
}

# Tornado chart for sensitivity analysis (UPP, damages, etc.)
# sensitivity: data.frame with columns parameter, low, high, base (optional)
plot_tornado <- function(sensitivity, base_value = NULL, title = "Sensitivity Analysis") {
  if (!requireNamespace("ggplot2", quietly = TRUE)) {
    stop("Install ggplot2 to create tornado charts.")
  }
  if (!all(c("parameter", "low", "high") %in% names(sensitivity))) {
    stop("sensitivity must have columns 'parameter', 'low', and 'high'")
  }

  # Calculate swing
  sensitivity$swing <- abs(sensitivity$high - sensitivity$low)
  sensitivity <- sensitivity[order(-sensitivity$swing), ]
  sensitivity$parameter <- factor(sensitivity$parameter, levels = sensitivity$parameter)

  # Reshape for plotting
  sens_long <- tidyr::pivot_longer(
    sensitivity,
    cols = c(low, high),
    names_to = "bound",
    values_to = "value"
  )

  p <- ggplot(sens_long, aes(x = value, y = parameter, fill = bound)) +
    geom_col(position = position_dodge(width = 0.7), width = 0.6) +
    scale_fill_manual(values = c(low = "#D55E00", high = "#0072B2"),
                      labels = c(low = "Low", high = "High")) +
    labs(title = title, x = "Value", y = NULL, fill = "Scenario") +
    theme_antitrust() +
    theme(legend.position = "bottom")

  if (!is.null(base_value)) {
    p <- p + geom_vline(xintercept = base_value, linetype = "dashed", color = "black")
  }

  p
}

# Sankey diagram for multi-homing, switching matrices, etc.
# flows: data.frame with columns from, to, value
plot_sankey <- function(flows, title = "Flow Diagram") {
  if (!requireNamespace("ggplot2", quietly = TRUE) ||
      !requireNamespace("ggsankey", quietly = TRUE)) {
    stop("Install ggplot2 and ggsankey to create Sankey diagrams.")
  }
  if (!all(c("from", "to", "value") %in% names(flows))) {
    stop("flows must have columns 'from', 'to', and 'value'")
  }

  p <- ggplot(flows, aes(x = from, next_x = to,
                         node = from, next_node = to,
                         fill = from, value = value)) +
    ggsankey::geom_sankey() +
    ggsankey::theme_sankey(base_size = 12) +
    labs(title = title, fill = "Source") +
    theme(legend.position = "bottom")

  p
}

# Quick BLS data pull
fetch_bls <- function(series_id, start_year = 2010, end_year = as.numeric(format(Sys.Date(), "%Y"))) {
  if (!requireNamespace("blsAPI", quietly = TRUE)) {
    stop("Install blsAPI to fetch BLS data.")
  }

  payload <- list(
    seriesid = series_id,
    startyear = start_year,
    endyear = end_year,
    registrationkey = Sys.getenv("BLS_KEY")
  )

  response <- blsAPI::blsAPI(payload, return_data_frame = TRUE)
  response$date <- as.Date(paste0(response$year, "-",
                                  sprintf("%02d", as.numeric(response$period)), "-01"))
  response$value <- as.numeric(response$value)
  response
}

# Quick Census API pull
fetch_census <- function(dataset, vintage = 2021, vars, region = "us:*") {
  if (!requireNamespace("censusapi", quietly = TRUE)) {
    stop("Install censusapi to fetch Census data.")
  }

  censusapi::getCensus(
    name = dataset,
    vintage = vintage,
    vars = vars,
    region = region,
    key = Sys.getenv("CENSUS_API_KEY")
  )
}
