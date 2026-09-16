"""
Practice Day 1
- Lorenz curve
"""

import numpy as np
import pandas as pd
import wbdata as wb
import matplotlib.pyplot as plt

np.random.seed(31) #Set the random seed for reproducibility

incomes = np.random.lognormal(mean = 1.5, sigma = 0.75, size = 1000) #Real-world data closely matches a lognormal distribution

sorted_incomes = np.sort(incomes)

p = np.linspace(0, 1, len(sorted_incomes) + 1) #p is cumulative population share

l = np.cumsum(sorted_incomes)/ np.sum(sorted_incomes) #L is cumulative income share
l = np.insert(l, 0, 0) #Insert 0 at the beginning of l

area = np.trapezoid(l, p)

gini = 1 - 2 * area 

print(f"Gini coefficient: {gini:.4f}")

#Apply the Lorenz curve to GDP Inequiality

from pathlib import Path

OUTPUT_PATH = Path(__file__).resolve().parent / "lorenz_gdp_countries.png"

def lorenz_and_gini(values):
    """
    values: 1D array of non-negative numbers
    The reasonn for the use of def function is that we have to consider several different datasets and wnat to avoid repeating the same code for each datasets.
    """
    sorted_values = np.sort(values)
    x = np.linspace(0, 1, len(sorted_values) + 1)
    y = np.cumsum(sorted_values) / np.sum(sorted_values)
    y = np.insert(y, 0, 0)
    area = np.trapezoid(y, x)
    gini = 1 - 2 * area
    return x, y, gini

YEAR = 2023 

all_countries = wb.get_countries()

individual_country_codes = [
    c["id"] for c in all_countries if c["region"]["value"] != "Aggregates"
]
gdp = wb.get_dataframe(
    {"NY.GDP.MKTP.CD": "gdp"},
    country=individual_country_codes,
    date=str(YEAR),
)
gdp = gdp.dropna()
 
gdp_values = gdp["gdp"].to_numpy()  # explicitly convert to a 1D array
print(f"Number of countries used in the analysis: {len(gdp_values)}")

x, y, gini = lorenz_and_gini(gdp.values)
print(f"Gini coefficient (Country GDP, {YEAR}): {gini:.4f}")

plt.figure(figsize=(6, 6))
plt.plot(x, y, label="Lorenz curve", color="steelblue")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Perfect equality")
plt.fill_between(x, y, x, color="lightblue", alpha=0.4)
plt.xlabel("Cumulative share of countries")
plt.ylabel("Cumulative share of world GDP")
plt.title(f"Lorenz Curve: Country GDP Inequality {YEAR} (Gini = {gini:.3f})")
plt.legend()
plt.gca().set_aspect("equal")
plt.tight_layout()
plt.savefig(OUTPUT_PATH, dpi=150)
print(f"Saved chart to: {OUTPUT_PATH}")
plt.show()