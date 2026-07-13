"""Worksheet: Charging Stations by Charger Type"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_sample_charging

df = load_sample_charging()
by_type = df["ChargerType"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(by_type.values, labels=by_type.index, autopct="%1.1f%%", startangle=90)
plt.title("Charging Stations by Charger Type")
plt.tight_layout()
plt.show()
