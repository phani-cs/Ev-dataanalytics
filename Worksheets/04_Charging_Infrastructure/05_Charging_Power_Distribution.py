"""Worksheet: Charging Power Distribution"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_sample_charging

df = load_sample_charging()

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Power_kW", bins=8, color="#2E86C1")
plt.title("Charging Power Distribution")
plt.xlabel("Power (kW)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
