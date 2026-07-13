"""Worksheet: Top Regions by Charging Stations"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_sample_charging

df = load_sample_charging()
top = (
    df.groupby("Region", as_index=False)
    .size()
    .rename(columns={"size": "Stations"})
    .sort_values("Stations", ascending=False)
)

plt.figure(figsize=(8, 5))
sns.barplot(data=top, y="Region", x="Stations", color="#C0392B", orient="h")
plt.title("Top Regions by Charging Stations")
plt.tight_layout()
plt.show()
