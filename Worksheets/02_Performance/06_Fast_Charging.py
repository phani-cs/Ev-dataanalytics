"""Worksheet: Fast Charging (Cheapest EV database)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_cheapest_ev

df = load_cheapest_ev().dropna(subset=["FastCharge_KmH"]).nlargest(15, "FastCharge_KmH")

plt.figure(figsize=(10, 7))
sns.barplot(data=df, y="Name", x="FastCharge_KmH", color="#E74C3C", orient="h")
plt.title("Fast Charging — Top 15 Models")
plt.xlabel("Fast Charge (Km/H)")
plt.ylabel("")
plt.tight_layout()
plt.show()
