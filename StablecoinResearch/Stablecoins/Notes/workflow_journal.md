# Stablecoin Research Workflow Journal

## Date: 2025-09-08

## **Objective**
To analyze the economic feasibility of a de-peg attack on an algorithmic stablecoin and propose effective mitigation measures to prevent or minimize its impact.

## **Goal**
1. **Understand De-Pegging**: Research past de-peg events and identify key factors contributing to such scenarios.
2. **Model Attack Feasibility**: Develop a framework to calculate the cost of executing a de-peg attack versus the potential profit for the attacker.
3. **Propose Mitigation Measures**: Design and evaluate mechanisms to prevent de-pegging or reduce its impact, including circuit breakers, enhanced liquidity reserves, and real-time monitoring systems.
4. **Document Findings**: Summarize the analysis, modeling, and proposed solutions in a clear and concise markdown file with supporting diagrams and data insights.

## **Workflow**

### Tasks Completed
- Set up folder structure for stablecoin research
- Added arxiv stablecoin scraper script to Tools
- Planned resource collection and analysis workflow
- Extracted titles from arxiv_stablecoin_papers.csv for analysis

### Scripts/Tools Used
- arxiv_stablecoin_scraper.py (arXiv API metadata scraper)
- Rainbow CSV for viewing and aligning CSV data
- Manual extraction of titles for further processing

### Insights & Challenges
- arXiv API provides useful metadata for academic papers
- Need to regularly update resource collection as new papers are published
- Titles extracted successfully for further analysis
- CSV file contains detailed metadata, which can be leveraged for deeper insights

### Next Steps
- Analyze collected papers and blogs
- Summarize findings in Analysis folder
- Continue documenting workflow and insights in this journal
- Perform analysis on extracted titles
- Use insights to categorize and summarize stablecoin research
- Document findings in the Analysis folder

---

## Date: 2025-09-17

### Tasks Completed
- Populated `requirements.txt` with all required third-party packages based on project imports
- Switched to the previous Python virtual environment (`.venv`) for consistent dependency management
- Set up GitHub remote and created a new feature branch for ongoing work
- Staged all local changes in preparation for commit
- Reviewed and planned improvements for the de-peg attack simulation, including:
	- Adding Monte Carlo logic for more realistic peg failure probability estimation
	- Outlining integration of DualTokenSim modules into the simulation
	- Drafting a new structure for the simulation function to support parameter sweeps and probabilistic outcomes


### Next Steps
- Commit and push changes to the new feature branch on GitHub
- Implement and test the improved simulation logic
- Generate updated plots and heatmaps reflecting the new simulation results
- Continue updating the workflow journal and documentation with progress and insights

---

## Date: 2025-09-16

### Tasks Completed
- Began implementation of a Monte Carlo de-peg attack simulation using DualTokenSim modules
- Created experiment script stub (`depeg_attack_experiment.py`) in Model/experiments/
- Set up outputs/ directory for simulation results
- Drafted initial model explanation in docs/model_explainer.md

### Next Steps
- Implement detailed simulation logic using DualTokenSim AMM and token modules
- Run experiments and generate heatmaps and summary statistics
- Update model explainer and workflow journal with results and insights

---


## Date: 2025-09-17 (continued)

### Tasks Completed
- Integrated real-world UST price data (May 2022 Terra collapse) using CoinGecko API
- Created and saved `fetch_ust_prices.py` to automate historical price data collection
- Developed and saved `terra_case_config.json` for empirical simulation parameterization
- Built overlay plotting script (`plot_ust_overlay.py`) to compare simulation output with real data
- Automated saving of overlay plot to `Stablecoins/Diagrams/ust_overlay.png` for documentation and publication
- Documented empirical workflow for reproducibility and academic rigor

### Insights & Challenges
- Real data integration strengthens model credibility and academic defensibility
- Overlay plots provide direct visual evidence of model fit to real-world events
- Data cleaning and column alignment require careful attention for seamless automation
- DeFiLlama pool data fetch script prepared but not used (user opted out)

### Next Steps
- Run full empirical case study: fetch real data, run sim with empirical config, generate overlay plot
- Document results and interpretation in Analysis and DataInsights folders
- Extend workflow to other stablecoin events (e.g., USDC-SVB, IRON Finance) as needed
- Continue updating workflow journal with empirical validation progress

---

*Update this journal regularly to track your research progress and decisions.*

---

*Update this journal regularly to track your research progress and decisions.*
