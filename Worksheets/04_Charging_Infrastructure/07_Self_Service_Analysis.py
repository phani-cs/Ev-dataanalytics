"""Worksheet: Self-Service Analysis — explore charging data"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils import load_sample_charging

df = load_sample_charging()

print("=== Self-Service Analysis: Charging Stations ===\n")
print("Total stations:", len(df))
print("\nBy Region:\n", df.groupby("Region").size().to_string())
print("\nBy Charger Type:\n", df.groupby("ChargerType").size().to_string())
print("\nAverage Power (kW) by Region:\n", df.groupby("Region")["Power_kW"].mean().round(1).to_string())
print("\nFull table:\n")
print(df.to_string(index=False))
