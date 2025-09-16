# Project File and Folder Change Log

This document tracks all major changes, additions, and population of folders/files in the Stablecoin Research project, from initial setup to the present.

---

## Initial Setup
- Created core project folder structure:
  - `Stablecoins/Analysis/`
  - `Stablecoins/DataInsights/`
  - `Stablecoins/Tools/`
  - `Stablecoins/Notes/`
  - `Stablecoins/Model/`, `Simulations/`, `Resources/`, etc.

---

## Analysis Folder (`Stablecoins/Analysis/`)
- Populated with:
  - Executive summary and research overview
  - Technical analysis and economic analysis documents
  - Attack scenario documentation
  - Comparative study and cross-model validation
  - Visualizations and publication-ready figures (heatmaps, time-series, validation plots)
  - README and navigation guide

---

## DataInsights Folder (`Stablecoins/DataInsights/`)
- Created and populated the following subfolders:
  - `statistical_analysis/`: Comprehensive statistics, hypothesis testing, variance decomposition, Monte Carlo validation
  - `pattern_recognition/`: Behavioral pattern analysis, predictive models, anomaly detection
  - `key_insights/`: Critical findings, counterintuitive results, policy recommendations
  - `raw_data/`: Raw simulation data documentation, empirical data scripts, config files
- Added a detailed `README.md` summarizing the structure and usage of the DataInsights package

---

## Tools Folder (`Stablecoins/Tools/`)
- Added scripts for:
  - Fetching real UST price data from CoinGecko (`fetch_ust_prices.py`)
  - Fetching Curve pool TVL from DeFiLlama (`fetch_curve_ust_tvl.py`)
  - Simulation configuration for empirical case studies (`terra_case_config.json`)
  - Overlay plotting of real vs. simulated data (`plot_ust_overlay.py`)
- Existing scripts for scraping and PDF processing retained

---

## Empirical Data Integration
- Automated fetching and saving of real-world data for empirical validation
- Created config files for parameterizing simulations with real event data
- Enabled direct visual comparison of model output and real market behavior

---

## Documentation and Navigation
- Added/updated `README.md` files in major folders for navigation and usage guidance
- Updated `workflow_journal.md` with all major workflow and empirical integration steps
- Created this change log for transparent project tracking

---

## Summary
- All previously empty or placeholder folders now contain comprehensive documentation, analysis, scripts, and data science resources
- Project is fully organized for academic, policy, and industry use, with reproducible workflows and empirical validation

---

*Last updated: 2025-09-17*
