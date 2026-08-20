# COVID-19 India: State-wise Data Analysis

A data analysis project exploring COVID-19 trends across major Indian states, 
focused on identifying regional disparities in case severity, fatality rates, 
vaccination coverage, and testing efficiency...

## What this project does
- Cleans and structures state-wise COVID-19 data using **SQL**
- Performs exploratory data analysis using **Python (Pandas)**
- Visualizes key metrics with **Matplotlib** — total cases, cases per million, 
  fatality rate, positivity rate, and cases vs. deaths comparison
- Identifies which states show signs of under-testing, higher severity, 
  and vaccination gaps

## Tech stack
- Python (Pandas, Matplotlib)
- SQL (MySQL)

## Key insights
- Delhi has the highest cases per million population despite not having 
  the highest raw case count — shows density matters more than total population
- Gujarat recorded the highest fatality rate among all analyzed states (1.35%)
- Kerala's high positivity rate (44.71%) suggests strong testing coverage 
  relative to population, catching more actual cases

## Files
- `queries.sql` — SQL table creation and analysis queries
- `analysis.py` — Python script for EDA and chart generation
- `chart_*.png` — Generated visualizations
