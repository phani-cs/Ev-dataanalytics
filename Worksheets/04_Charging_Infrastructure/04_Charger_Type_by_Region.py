"""Worksheet: Charger Type by Region"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_sample_charging

df = load_sample_charging()
ct = pd.crosstab(df["Region"], df["ChargerType"])

ct.plot(kind="bar", stacked=True, figsize=(9, 5))
plt.title("Charger Type by Region")
plt.xlabel("Region")
plt.ylabel("Stations")
plt.xticks(rotation=0)
plt.legend(title="Charger Type")
plt.tight_layout()
plt.show()
