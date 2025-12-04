# Data folder

Use this directory as the clearinghouse for every dataset referenced in the book or live matters. Pair each asset with a short provenance note so anyone can rebuild the analysis months later.

## Structure

- `raw/`: downloads from APIs or third parties. Keep immutable; include a short `*_notes.txt` per dataset with source, request ID, and legal restrictions.
- `derived/`: cleaned/aggregated data ready for analysis (`arrow` parquet or documented CSV). Mirror the inventory fields described in `chapters/13-empirical-appendix.qmd`.
- `README.md` (this file): catalog of flagship assets and handling rules.
- Do not commit actual data; `.gitignore` already excludes both subfolders.

## Collected datasets (as of 2025-11-24)

### FRED Economic Data (raw/)
✓ **Collected** - 15 time series from Federal Reserve Economic Data
- Bank concentration (HHI): `fred_bank_hhi.csv`
- Retail & manufacturing HHI: `fred_retail_hhi.csv`, `fred_mfg_hhi.csv`
- Price series for cartel screens: gasoline, crude oil, bread, wheat, steel, cement
- Labor indicators: wages, LFPR, JOLTS
- Inflation indices: CPI, PPI, import prices
- **Metadata:** `fred_metadata.csv`
- **Chapters:** 01, 02, 03, 04, 05, 10

### Financial Data (raw/)
✓ **Collected** - Stock prices for event studies (2010-present)
- Airlines: `finance_airlines.csv` (AAL, DAL, LUV, UAL, JBLU, ALK, SPY)
- Tech platforms: `finance_tech_platforms.csv` (GOOGL, META, AMZN, AAPL, MSFT, NFLX)
- Healthcare: `finance_healthcare.csv` (insurers, pharma, hospital chains)
- Telecom: `finance_telecom.csv` (T, VZ, TMUS, CHTR, CMCSA)
- Retail: `finance_retail.csv` (WMT, TGT, COST, KR, ACI)
- **Metadata:** `finance_metadata.csv`
- **Chapters:** 02, 06, 08, 09, 11

### Airline Market Data (derived/)
✓ **Collected** - nycflights13 analysis
- Route shares & HHI: `airline_route_shares.csv` (439 route-carrier pairs)
- Hub concentration: `airline_hub_concentration.csv` (3 NYC airports)
- Carrier metrics: `airline_carrier_metrics.csv` (16 carriers)
- Hourly patterns: `airline_hourly_patterns.csv`
- Delay analysis: `airline_delay_analysis.csv`
- **Metadata:** `flights_metadata.csv`
- **Chapters:** 03, 06

### Cartel Screening Data (derived/)
✓ **Collected** - Synthetic examples for methodology demonstration
- Bread cartel prices: `cartel_bread_prices.csv` (structural break example)
- Cement bid rotation: `cartel_cement_bids.csv` (200 projects, 2010-2023)
- Price correlation: `cartel_price_correlation.csv` (variance screen)
- Rotation metrics: `cartel_rotation_metrics.csv`
- **Metadata:** `procurement_cartels_metadata.csv`
- **Chapters:** 05
- **Note:** Replace with real data from Stats SA or competition authority filings

### Digital Platforms (derived/)
✓ **Collected** - Market shares from public filings + synthetic usage data
- Market shares: `platform_market_shares.csv` (6 cases: Google, Amazon, Meta, Apple)
- Commission rates: `platform_commission_rates.csv` (App Store, Google Play, Amazon)
- Two-sided usage: `platform_two_sided_usage.csv` (network effects simulation)
- Search ranking: `platform_search_ranking.csv` (self-preferencing metrics)
- Default effects: `platform_default_effects.csv`
- Multi-homing: `platform_multihoming_users.csv`, `platform_multihoming_summary.csv`
- **Metadata:** `digital_platforms_metadata.csv`
- **Chapters:** 09

### Regulation & Benchmarking (derived/)
✓ **Collected** - Utility tariffs and regulatory examples
- Utility benchmarking: `utility_benchmarking.csv` (120 utility-years, 3 regimes)
- Access pricing: `access_pricing_examples.csv` (LRIC, ECPR examples from UK, US, EU, SA)
- Incentive schemes: `regulatory_incentive_schemes.csv` (rate-of-return vs price-cap)
- Remedy monitoring: `remedy_monitoring.csv` (post-merger compliance)
- SA regulation: `sa_regulatory_examples.csv` (ICASA, NERSA, Competition Commission)
- **Metadata:** `regulation_benchmarks_metadata.csv`
- **Chapters:** 08

## Pending / manual download required

| Asset | Source / contact | Status | Notes |
| --- | --- | --- | --- |
| PatentsView data | https://patentsview.org/download/ | ⚠ API deprecated | Download bulk files: patents.tsv, cpc_current.tsv |
| FDA Orange Book | https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files | ⚠ URL changed | Download products.txt, patent.txt, exclusivity.txt |
| BLS QCEW county data | https://www.bls.gov/cew/downloadable-data-files.htm | ⚠ Large files | Download annual CSVs for HHI calculation |
| World Bank procurement | https://finances.worldbank.org/Procurement/Major-Contract-Awards/kdui-wcs3 | ⚠ API changed | Export as CSV |
| OECD broadband prices | https://www.oecd.org/digital/broadband/broadband-statistics/ | ⚠ Manual | Download Excel file, see `raw/oecd_broadband_notes.txt` |
| Stats SA data | http://www.statssa.gov.za/ | ⚠ Access required | CPI micro-data, QLFS labor force survey |
| US hospital claims panel | CMS LDS or FAIR Health extracts | Future | Merger retrospectives, labor monopsony |
| South African retailer transactions | Competition Commission SA data requests | Future | Market definition, cartel screens |
| EU procurement & bid logs | TED / DG COMP data rooms | Future | Collusion screens, remedy monitoring |

## API Keys Required

To enable full data collection, register for free API keys:
- **FRED:** https://fred.stlouisfed.org/docs/api/api_key.html
- **BLS:** https://www.bls.gov/developers/home.htm

See `API_KEYS_SETUP.md` for detailed instructions.

## Intake checklist

1. Create `data/raw/<dataset>/README.md` capturing source, coverage, request letters, and applicable confidentiality orders.
2. Register the dataset in the appendix inventory tibble (see `chapters/13-empirical-appendix.qmd`).
3. Store transformation scripts in `scripts/` or `R/` with deterministic seeds and logging.
4. Push sanitized metadata (row counts, summary stats) into the book or expert reports when needed—never commit the underlying confidential data.

Refer back to `_literature/_0intro/Copy of ftcperspectivesoneconometrics.pdf` and `notes and slides/Copy of Research_Methods_2024.html` for examples of how agencies describe data handling in litigation records.
