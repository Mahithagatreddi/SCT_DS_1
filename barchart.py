import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "data/API_SP.POP.TOTL_DS2_en_csv_v2_430662.csv",
    skiprows=4
)

# Latest year
latest_year = "2023"

# Select required columns
population = df[["Country Name", "Country Code", latest_year]]

# Remove missing values
population = population.dropna()

# Remove aggregate regions
population = population[
    ~population["Country Name"].isin([
        "World",
        "IDA & IBRD total",
        "IBRD only",
        "IDA total",
        "Low income",
        "Lower middle income",
        "Upper middle income",
        "Middle income",
        "Low & middle income",
        "East Asia & Pacific",
        "Europe & Central Asia",
        "North America",
        "South Asia",
        "Sub-Saharan Africa",
        "Early-demographic dividend",
        "Late-demographic dividend"
    ])
]

# Sort by population
top10 = population.sort_values(
    by=latest_year,
    ascending=False
).head(10)

# Create Bar Chart
plt.figure(figsize=(12, 6))

plt.bar(
    top10["Country Name"],
    top10[latest_year]
)

plt.title("Top 10 Most Populated Countries (2023)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45)

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()

plt.savefig("top10_population.png")

plt.show()