"""Worksheet: Top 10 Most Efficient EV Brands"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()
# Lower Wh/Km = better efficiency
eff = (
    df.groupby("Brand", as_index=False)["Efficiency_WhKm"]
    .mean()
    .nsmallest(10, "Efficiency_WhKm")
)

plt.figure(figsize=(10, 6))
sns.barplot(data=eff, y="Brand", x="Efficiency_WhKm", color="#27AE60", orient="h")
plt.title("Top 10 Most Efficient EV Brands (Avg Wh/Km)")
plt.xlabel("Average Efficiency (Wh/Km)")
plt.ylabel("")
plt.tight_layout()
plt.show()
