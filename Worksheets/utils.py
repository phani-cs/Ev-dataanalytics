"""Shared helpers for EV worksheet scripts."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"


def load_global_ev() -> pd.DataFrame:
    df = pd.read_csv(DATA / "ElectricCarData_Clean.csv")
    df["Brand"] = df["Brand"].str.strip()
    df["Model"] = df["Model"].str.strip()
    for col in ["FastCharge_KmH"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def load_india_ev() -> pd.DataFrame:
    df = pd.read_csv(DATA / "EVIndia.csv")
    df["Range_Km"] = (
        df["Range"]
        .astype(str)
        .str.extract(r"(\d+)", expand=False)
        .astype(float)
    )
    df["BootSpace_L"] = (
        df["BootSpace"]
        .astype(str)
        .str.extract(r"(\d+)", expand=False)
        .astype(float)
    )
    df["Price_Lakhs"] = pd.to_numeric(df["PriceRange(Lakhs)"], errors="coerce")
    return df


def load_sample_charging() -> pd.DataFrame:
    """Sample charging-station data (original source was Tableau Hyper)."""
    rows = [
        ("North", "CCS", 50, 28.61, 77.21),
        ("North", "Type 2", 22, 28.70, 77.10),
        ("South", "CCS", 60, 12.97, 77.59),
        ("South", "CHAdeMO", 50, 13.08, 80.27),
        ("West", "CCS", 120, 19.07, 72.87),
        ("West", "Type 2", 22, 18.52, 73.85),
        ("East", "CCS", 50, 22.57, 88.36),
        ("East", "Type 2", 11, 23.34, 85.31),
        ("Central", "CCS", 60, 23.25, 77.41),
        ("Central", "Type 2", 22, 26.21, 78.18),
        ("North", "CCS", 150, 30.73, 76.78),
        ("South", "Type 2", 22, 11.01, 76.96),
        ("West", "CHAdeMO", 50, 21.14, 79.08),
        ("East", "CCS", 90, 25.59, 85.13),
        ("Central", "CCS", 50, 22.71, 75.85),
    ]
    return pd.DataFrame(
        rows, columns=["Region", "ChargerType", "Power_kW", "Latitude", "Longitude"]
    )
