"""Worksheet: Charging Stations by Region"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_sample_charging

df = load_sample_charging()
by_region = df.groupby("Region", as_index=False).size().rename(columns={"size": "Stations"})

plt.figure(figsize=(8, 5))
sns.barplot(data=by_region, x="Region", y="Stations", color="#E97627")
plt.title("Charging Stations by Region")
plt.tight_layout()
plt.show()
