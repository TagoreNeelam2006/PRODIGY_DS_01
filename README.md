# PRODIGY_DS_01

**Data Science Internship — Task 1**
Prodigy InfoTech

## 📌 Task
Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population.

## 📊 Dataset
**World Bank — Population, total** (indicator `SP.POP.TOTL`), from the World Development Indicators.
File used: `world_bank_population.csv` (originally `API_SP_POP_TOTL_DS2_en_csv_v2_38144.csv`)

The raw file contains:
- 4 metadata rows before the actual header (handled with `skiprows=4`)
- One row per country/region, with yearly population columns from 1960 to 2024
- 266 total rows, of which **49 are regional or income-group aggregates** (e.g. "World", "East Asia & Pacific", "High income") rather than individual countries — these are filtered out before analysis, leaving **217 individual countries**

## 🛠️ Tech Stack
- Python 3
- pandas — data loading & cleaning
- matplotlib & seaborn — visualization

## 📁 Repository Structure
```
PRODIGY_DS_01/
├── world_bank_population.csv          # source dataset
├── task1_visualization.py             # main analysis + chart generation script
├── population_distribution_histogram.png  # histogram of 2024 population (log scale)
├── top15_countries_barchart.png       # bar chart of the 15 most populous countries
├── top5_growth_trend.png              # bonus: population growth trend, top 5 countries
└── README.md
```

## ▶️ How to Run
```bash
pip install pandas matplotlib seaborn
python task1_visualization.py
```

## 📈 Visualizations

### 1. Population Distribution (Histogram, continuous variable)
Distribution of 2024 population across 217 countries, plotted on a **log scale**. Population values span from under 10,000 (small island nations) to over 1.4 billion (China, India) — a linear scale would compress nearly every country into a single bar near zero, so log scale is essential to see the actual shape of the distribution.

### 2. Top 15 Most Populous Countries (Bar Chart, categorical view)
Horizontal bar chart ranking the 15 largest countries by 2024 population.

### 3. Population Growth Trend — Top 5 Countries (Bonus, line chart)
Tracks how the five most populous countries' populations have changed every 5 years from 1970 to 2024, showing different growth trajectories (e.g. India's continued growth vs. slower/plateauing growth elsewhere).

## 💡 Key Insights
- Population is heavily right-skewed: the median country has ~6.6 million people, but the mean is dragged up to ~37 million by a small number of very large countries — the top quartile alone starts at ~27 million.
- China and India together account for a disproportionate share of world population, each exceeding 1.4 billion in 2024.
- Long-term growth trends diverge sharply between the largest countries — some show steady, near-linear growth, others have visibly slowed in recent decades.

## 🔗 About
This repository is part of my Data Science Internship at **Prodigy InfoTech**.

#DataScience #Python #DataVisualization #ProdigyInfoTech #Internship
