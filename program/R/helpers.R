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
  api_key <- Sys.getenv("FRED_API_KEY")
  if (is.null(api_key) || nchar(api_key) == 0) {
    stop("FRED_API_KEY not set. Add it to .Renviron (see .Renviron.example).")
  }
  fredr::fredr_set_key(api_key)
  fredr::fredr(series_id = series_id, observation_start = start)
}

# Simple differentiated products logit simulation (static, no nests) for teaching.
# products: data.frame with columns product, firm, price, share, mc (or margin)
run_logit_sim <- function(products, merging_firms) {
  stopifnot(all(c("product", "firm", "price", "share") %in% names(products)))
  if (!"mc" %in% names(products)) {
    stop("Provide marginal costs in column `mc` (or add price * (1 - margin)).")
  }
  if (length(merging_firms) < 2) {
    stop("merging_firms must contain at least two firm names.")
  }
  missing_firms <- setdiff(merging_firms, products$firm)
  if (length(missing_firms) > 0) {
    stop("merging_firms not found in products$firm: ",
         paste(missing_firms, collapse = ", "))
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
  if (!requireNamespace("ggsankey", quietly = TRUE)) {
    stop("Install ggsankey to create Sankey diagrams.")
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

# Quick BLS data pull.
# BLS period field uses format "M01"..."M12" for monthly data; strip the "M" prefix
# before converting to a numeric month for date construction.
fetch_bls <- function(series_id, start_year = 2010, end_year = as.numeric(format(Sys.Date(), "%Y"))) {
  if (!requireNamespace("blsAPI", quietly = TRUE)) {
    stop("Install blsAPI to fetch BLS data.")
  }
  api_key <- Sys.getenv("BLS_KEY")
  if (is.null(api_key) || nchar(api_key) == 0) {
    stop("BLS_KEY not set. Add it to .Renviron (see .Renviron.example).")
  }

  payload <- list(
    seriesid = series_id,
    startyear = start_year,
    endyear = end_year,
    registrationkey = api_key
  )

  response <- blsAPI::blsAPI(payload, return_data_frame = TRUE)
  # BLS period field is "M01", "M02", etc. -- strip the leading letter(s)
  month_num <- as.numeric(gsub("[^0-9]", "", response$period))
  response$date <- as.Date(paste0(response$year, "-",
                                  sprintf("%02d", month_num), "-01"))
  response$value <- as.numeric(response$value)
  response
}

#' Quick Census API pull
#'
#' @param dataset Character. Census dataset name (e.g., "acs/acs5")
#' @param vintage Integer. Year of the dataset
#' @param vars Character vector. Variables to retrieve
#' @param region Character. Geographic region specification
#' @return Data frame with Census data
fetch_census <- function(dataset, vintage = 2021, vars, region = "us:*") {
  if (!requireNamespace("censusapi", quietly = TRUE)) {
    stop("Install censusapi to fetch Census data.")
  }
  api_key <- Sys.getenv("CENSUS_API_KEY")
  if (is.null(api_key) || nchar(api_key) == 0) {
    stop("CENSUS_API_KEY not set. Add it to .Renviron (see .Renviron.example).")
  }

  censusapi::getCensus(
    name = dataset,
    vintage = vintage,
    vars = vars,
    region = region,
    key = api_key
  )
}

#' Waterfall chart for cumulative changes (e.g., HHI, royalty stacks)
#'
#' Creates a waterfall chart showing how values accumulate or change across
#' categories. Useful for merger HHI analysis, royalty stacks, and damages
#' decompositions.
#'
#' @param data Data frame with columns: category (character), value (numeric)
#' @param category_col Character. Name of column with category labels
#' @param value_col Character. Name of column with numeric values
#' @param fill_col Character. Optional column for fill color grouping
#' @param title Character. Plot title
#' @param subtitle Character. Plot subtitle
#' @param y_label Character. Y-axis label
#' @param show_connector Logical. Show dashed lines connecting bars
#' @param total_label Character. Label for the total bar (NULL to omit)
#' @return A ggplot2 object
#'
#' @examples
#' # HHI change waterfall
#' hhi_data <- tibble::tibble(
#'   category = c("Pre-merger HHI", "Lost competition", "Post-merger HHI"),
#'   value = c(1800, 400, NA)
#' )
#' plot_waterfall(hhi_data, "category", "value", title = "HHI Change")
plot_waterfall <- function(data,
                           category_col = "category",
                           value_col = "value",
                           fill_col = NULL,
                           title = "Waterfall Chart",
                           subtitle = NULL,
                           y_label = "Value",
                           show_connector = TRUE,
                           total_label = NULL) {

  # Prepare data with cumulative values
  df <- data.frame(
    cat = data[[category_col]],
    val = data[[value_col]]
  )

  # Calculate running totals for waterfall positioning
  df$end <- cumsum(df$val)
  df$start <- c(0, head(df$end, -1))

  # Add total bar if requested
  if (!is.null(total_label)) {
    total_row <- data.frame(
      cat = total_label,
      val = df$end[nrow(df)],
      start = 0,
      end = df$end[nrow(df)]
    )
    df <- rbind(df, total_row)
  }

  # Preserve category order
  df$cat <- factor(df$cat, levels = df$cat)

  # Color by increase/decrease

  df$direction <- ifelse(df$val >= 0, "Increase", "Decrease")

  p <- ggplot2::ggplot(df) +
    ggplot2::geom_rect(
      ggplot2::aes(
        xmin = as.numeric(cat) - 0.4,
        xmax = as.numeric(cat) + 0.4,
        ymin = start,
        ymax = end,
        fill = direction
      ),
      color = "white",
      linewidth = 0.5
    )

  # Add connector lines between bars
  if (show_connector && nrow(df) > 1) {
    connectors <- df[-nrow(df), ]
    connectors$x_start <- as.numeric(factor(connectors$cat, levels = levels(df$cat))) + 0.4
    connectors$x_end <- connectors$x_start + 0.2

    p <- p + ggplot2::geom_segment(
      data = connectors,
      ggplot2::aes(x = x_start, xend = x_end, y = end, yend = end),
      linetype = "dashed",
      color = "gray50",
      linewidth = 0.5
    )
  }

  # Add value labels centered in each bar
  p <- p + ggplot2::geom_text(
    ggplot2::aes(
      x = as.numeric(cat),
      y = (start + end) / 2,
      label = round(val, 0)
    ),
    size = 3.5,
    fontface = "bold"
  )

  # Style the plot
  p <- p +
    ggplot2::scale_x_continuous(
      breaks = seq_along(levels(df$cat)),
      labels = levels(df$cat)
    ) +
    ggplot2::scale_fill_manual(
      values = c("Increase" = "#D55E00", "Decrease" = "#0072B2"),
      guide = "none"
    ) +
    ggplot2::labs(
      title = title,
      subtitle = subtitle,
      x = NULL,
      y = y_label
    ) +
    theme_antitrust() +
    ggplot2::theme(
      axis.text.x = ggplot2::element_text(angle = 45, hjust = 1),
      legend.position = "none"
    )

  p
}

#' Calculate HHI and change from market share data
#'
#' Computes HHI before and after a merger, with the change (delta HHI).
#' Uses the 2023 Merger Guidelines thresholds:
#' - HHI < 1,500: Unconcentrated
#' - HHI 1,500-2,500: Moderately concentrated
#' - HHI > 2,500: Highly concentrated
#' - Delta HHI > 100: May warrant scrutiny
#'
#' @param shares Data frame with columns: firm, share (as decimal 0-1)
#' @param merging_firms Character vector of merging firm names
#' @return List with pre_hhi, post_hhi, delta_hhi, and shares_post data frame
#'
#' @examples
#' shares <- tibble::tibble(
#'   firm = c("A", "B", "C", "D"),
#'   share = c(0.30, 0.25, 0.20, 0.25)
#' )
#' calc_hhi_change(shares, c("A", "B"))
calc_hhi_change <- function(shares, merging_firms) {
  stopifnot(all(c("firm", "share") %in% names(shares)))

  # Convert to percentages for HHI calculation (shares * 100)
  shares$share_pct <- shares$share * 100

  # Pre-merger HHI: sum of squared market shares
  pre_hhi <- sum(shares$share_pct^2)

  # Post-merger: combine merging firms' shares
  merged_share <- sum(shares$share_pct[shares$firm %in% merging_firms])
  merged_name <- paste(merging_firms, collapse = "+")

  shares_post <- shares[!shares$firm %in% merging_firms, ]
  shares_post <- rbind(
    shares_post,
    data.frame(
      firm = merged_name,
      share = merged_share / 100,
      share_pct = merged_share
    )
  )

  # Post-merger HHI
  post_hhi <- sum(shares_post$share_pct^2)

  list(
    pre_hhi = round(pre_hhi, 0),
    post_hhi = round(post_hhi, 0),
    delta_hhi = round(post_hhi - pre_hhi, 0),
    shares_post = shares_post
  )
}
