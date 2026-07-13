"""Worksheet: Range Comparison (India EVs)"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_india_ev

df = load_india_ev().sort_values("Range_Km", ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(data=df, y="Car", x="Range_Km", color="#16A085", orient="h")
plt.title("Range Comparison — India EVs")
plt.xlabel("Range (Km)")
plt.ylabel("")
plt.tight_layout()
plt.show()
