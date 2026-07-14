"""Shared helpers for EV worksheet scripts and the web app."""
from pathlib import Path
import re
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"


def load_global_ev() -> pd.DataFrame:
    """Dataset 1: ElectricCarData_Clean"""
    df = pd.read_csv(DATA / "ElectricCarData_Clean.csv")
    df["Brand"] = df["Brand"].astype(str).str.strip()
    df["Model"] = df["Model"].astype(str).str.strip()
    for col in ["FastCharge_KmH", "AccelSec", "TopSpeed_KmH", "Range_Km", "Efficiency_WhKm", "PriceEuro"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def load_india_ev() -> pd.DataFrame:
    """Dataset 2: EVIndia"""
    df = pd.read_csv(DATA / "EVIndia.csv")
    df["Range_Km"] = (
        df["Range"].astype(str).str.extract(r"(\d+)", expand=False).astype(float)
    )
    df["BootSpace_L"] = (
        df["BootSpace"].astype(str).str.extract(r"(\d+)", expand=False).astype(float)
    )
    df["Price_Lakhs"] = pd.to_numeric(df["PriceRange(Lakhs)"], errors="coerce")
    return df


def load_cheapest_ev() -> pd.DataFrame:
    """Dataset 3: Cheapestelectriccars-EVDatabase"""
    df = pd.read_csv(DATA / "Cheapestelectriccars-EVDatabase.csv")

    def _num(series: pd.Series) -> pd.Series:
        return (
            series.astype(str)
            .str.replace(r"[^0-9.]", "", regex=True)
            .replace({"": None, "nan": None, "N/A": None})
            .pipe(pd.to_numeric, errors="coerce")
        )

    df["Acceleration_sec"] = _num(df["Acceleration"])
    df["TopSpeed_KmH"] = _num(df["TopSpeed"])
    df["Range_Km"] = _num(df["Range"])
    df["Efficiency_WhKm"] = _num(df["Efficiency"])
    df["FastCharge_KmH"] = _num(df["FastChargeSpeed"])
    df["Price_Germany"] = _num(df.get("PriceinGermany", pd.Series(dtype=str)))
    df["Price_UK"] = _num(df.get("PriceinUK", pd.Series(dtype=str)))
    df["Brand"] = df["Name"].astype(str).str.split().str[0]
    df["Drive"] = df["Drive"].astype(str).str.strip()
    return df


def load_charging_stations() -> pd.DataFrame:
    """Dataset 4: electric_vehicle_charging_station_list"""
    df = pd.read_csv(DATA / "electric_vehicle_charging_station_list.csv")
    df["Power_kW"] = pd.to_numeric(df["Power_kW"], errors="coerce")
    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
    # aliases used by older worksheet scripts
    df["Region"] = df["Region"].astype(str)
    df["ChargerType"] = df["Charger_Type"].astype(str)
    return df


# backward-compatible alias
def load_sample_charging() -> pd.DataFrame:
    return load_charging_stations()
