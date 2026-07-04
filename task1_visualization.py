"""
Task 1 - PRODIGY_DS_01
------------------------
Create a bar chart or histogram to visualize the distribution of a
categorical or continuous variable, using the World Bank's
"Population, total" dataset (SP.POP.TOTL).

Dataset file: world_bank_population.csv
Source: World Bank World Development Indicators
        (file: API_SP_POP_TOTL_DS2_en_csv_v2_38144.csv)

This file mixes individual countries together with regional/income-group
aggregates (e.g. "World", "East Asia & Pacific", "High income"). Those
aggregates are excluded below so the visualizations reflect only actual
countries.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# ---------------------------------------------------------
# 1. Load the dataset
#    The real World Bank export has 4 metadata rows before the
#    actual header row, so we skip them.
# ---------------------------------------------------------
df = pd.read_csv("world_bank_population.csv", skiprows=4)

print("Raw dataset shape:", df.shape)
print("Columns (first 10):", df.columns.tolist()[:10])

# Drop the trailing unnamed empty column the World Bank export includes
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# ---------------------------------------------------------
# 2. Remove regional/income-group aggregates
#    The World Bank bundles ~48 aggregate rows (e.g. "World",
#    "European Union", "Low income") alongside real countries.
#    We exclude them by name so our variable represents individual
#    countries only.
# ---------------------------------------------------------
AGGREGATES = {
    "Africa Eastern and Southern", "Africa Western and Central", "Arab World",
    "Caribbean small states", "Central Europe and the Baltics",
    "Early-demographic dividend", "East Asia & Pacific (excluding high income)",
    "East Asia & Pacific", "Euro area", "Europe & Central Asia (excluding high income)",
    "Europe & Central Asia", "European Union", "Fragile and conflict affected situations",
    "High income", "Heavily indebted poor countries (HIPC)", "IBRD only",
    "IDA & IBRD total", "IDA total", "IDA blend", "IDA only", "Not classified",
    "Latin America & Caribbean (excluding high income)", "Latin America & Caribbean",
    "Least developed countries: UN classification", "Low income",
    "Lower middle income", "Low & middle income", "Late-demographic dividend",
    "Middle East, North Africa, Afghanistan & Pakistan", "Middle income",
    "Middle East, North Africa, Afghanistan & Pakistan (excluding high income)",
    "North America", "OECD members", "Other small states", "Pre-demographic dividend",
    "Pacific island small states", "Post-demographic dividend", "South Asia",
    "Sub-Saharan Africa (excluding high income)", "Sub-Saharan Africa", "Small states",
    "East Asia & Pacific (IDA & IBRD countries)", "Europe & Central Asia (IDA & IBRD countries)",
    "Latin America & the Caribbean (IDA & IBRD countries)",
    "Middle East, North Africa, Afghanistan & Pakistan (IDA & IBRD)",
    "South Asia (IDA & IBRD)", "Sub-Saharan Africa (IDA & IBRD countries)",
    "Upper middle income", "World",
}

df_countries = df[~df["Country Name"].isin(AGGREGATES)].copy()
print(f"\nRemoved {len(df) - len(df_countries)} aggregate rows, "
      f"{len(df_countries)} individual countries remain")

# ---------------------------------------------------------
# 3. Pick the year to analyze and clean it
# ---------------------------------------------------------
YEAR = "2024"  # most recent year with data in this file

df_countries = df_countries.dropna(subset=[YEAR])
df_countries[YEAR] = df_countries[YEAR].astype(float).astype(int)

print(f"\n{len(df_countries)} countries have data for {YEAR}")
print(df_countries[["Country Name", YEAR]].describe())

# ---------------------------------------------------------
# 4. Histogram — Population distribution (continuous variable)
#    Log scale because a handful of countries (China, India) are
#    orders of magnitude larger than most others.
# ---------------------------------------------------------
plt.figure(figsize=(9, 6))
sns.histplot(data=df_countries, x=YEAR, bins=25, kde=True, color="#4C72B0", edgecolor="black")
plt.xscale("log")
plt.title(f"Distribution of Country Populations ({YEAR})", fontsize=15, fontweight="bold")
plt.xlabel("Population (log scale)")
plt.ylabel("Number of Countries")
plt.tight_layout()
plt.savefig("population_distribution_histogram.png", dpi=200)
plt.close()
print("Saved population_distribution_histogram.png")

# ---------------------------------------------------------
# 5. Bar chart — Top 15 most populous countries (categorical view)
# ---------------------------------------------------------
plt.figure(figsize=(10, 7))
top15 = df_countries.nlargest(15, YEAR).sort_values(YEAR)
plt.barh(top15["Country Name"], top15[YEAR], color=sns.color_palette("viridis", 15))
plt.title(f"Top 15 Most Populous Countries ({YEAR})", fontsize=15, fontweight="bold")
plt.xlabel("Population")
for i, v in enumerate(top15[YEAR]):
    plt.text(v, i, f" {v/1e6:.0f}M", va="center", fontweight="bold", fontsize=9)
plt.tight_layout()
plt.savefig("top15_countries_barchart.png", dpi=200)
plt.close()
print("Saved top15_countries_barchart.png")

# ---------------------------------------------------------
# 6. Bonus — Population growth over time for the 5 largest countries
# ---------------------------------------------------------
YEARS_TO_PLOT = [str(y) for y in range(1970, 2025, 5)]
top5_names = df_countries.nlargest(5, YEAR)["Country Name"].tolist()
trend_df = df_countries[df_countries["Country Name"].isin(top5_names)]

plt.figure(figsize=(10, 6))
for _, row in trend_df.iterrows():
    values = [float(row[y]) for y in YEARS_TO_PLOT]
    plt.plot(YEARS_TO_PLOT, values, marker="o", label=row["Country Name"])
plt.title("Population Growth Over Time — Top 5 Countries", fontsize=15, fontweight="bold")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.tight_layout()
plt.savefig("top5_growth_trend.png", dpi=200)
plt.close()
print("Saved top5_growth_trend.png")

print("\nAll visualizations generated successfully.")
