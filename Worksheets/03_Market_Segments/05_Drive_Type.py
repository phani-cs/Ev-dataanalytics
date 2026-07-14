"""Worksheet: Drive Type (from Cheapest EV database)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_cheapest_ev

df = load_cheapest_ev()
pt = df["Drive"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(pt.values, labels=pt.index, autopct="%1.1f%%", startangle=90)
plt.title("Drive Type Distribution")
plt.tight_layout()
plt.show()
