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
