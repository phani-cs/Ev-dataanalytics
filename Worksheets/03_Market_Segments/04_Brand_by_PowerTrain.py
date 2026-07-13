"""Worksheet: Brand by PowerTrain"""
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_global_ev

df = load_global_ev()
ct = pd.crosstab(df["Brand"], df["PowerTrain"])

ct.plot(kind="bar", stacked=True, figsize=(12, 6))
plt.title("Brand by PowerTrain")
plt.xlabel("Brand")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.legend(title="PowerTrain", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.show()
