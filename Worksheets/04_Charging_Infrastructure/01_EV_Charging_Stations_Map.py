"""Worksheet: EV Charging Stations Map"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_sample_charging

df = load_sample_charging()

plt.figure(figsize=(9, 8))
sns.scatterplot(data=df, x="Longitude", y="Latitude", hue="Region", style="ChargerType", s=120)
plt.title("EV Charging Stations Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()
