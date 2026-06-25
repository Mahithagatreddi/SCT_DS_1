import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    "data/API_SP.POP.TOTL_DS2_en_csv_v2_430662.csv",
    skiprows=4
)

# Use latest year available
latest_year = "2023"

# Remove missing values
population = df[latest_year].dropna()

# Create Histogram
plt.figure(figsize=(10, 6))

plt.hist(
    population,
    bins=20,
    edgecolor="black"
)

plt.title("Distribution of Country Populations")
plt.xlabel("Population")
plt.ylabel("Number of Countries")

plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.tight_layout()

plt.savefig("population_histogram.png")

plt.show()