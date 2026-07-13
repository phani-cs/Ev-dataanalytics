"""Worksheet: Efficiency"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

# Lower Wh/Km = more efficient
df = load_global_ev().nsmallest(15, "Efficiency_WhKm").copy()
df["Label"] = df["Brand"] + " " + df["Model"]

plt.figure(figsize=(10, 7))
sns.barplot(data=df, y="Label", x="Efficiency_WhKm", color="#1ABC9C", orient="h")
plt.title("Most Efficient EVs (Lowest Wh/Km)")
plt.xlabel("Efficiency (Wh/Km)")
plt.ylabel("")
plt.tight_layout()
plt.show()
