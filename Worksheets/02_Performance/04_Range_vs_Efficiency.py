"""Worksheet: Range vs Efficiency"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Efficiency_WhKm", y="Range_Km", hue="Segment", s=80)
plt.title("Range vs Efficiency")
plt.xlabel("Efficiency (Wh/Km)")
plt.ylabel("Range (Km)")
plt.tight_layout()
plt.show()
