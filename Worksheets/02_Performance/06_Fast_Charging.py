"""Worksheet: Fast Charging"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev().dropna(subset=["FastCharge_KmH"]).nlargest(15, "FastCharge_KmH").copy()
df["Label"] = df["Brand"] + " " + df["Model"]

plt.figure(figsize=(10, 7))
sns.barplot(data=df, y="Label", x="FastCharge_KmH", color="#E74C3C", orient="h")
plt.title("Fast Charging — Top 15 Models")
plt.xlabel("Fast Charge (Km/H)")
plt.ylabel("")
plt.tight_layout()
plt.show()
