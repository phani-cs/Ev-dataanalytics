<div align="center">

# ⚡ EV Data Analytics — Tableau Dashboard

### 🚗🔋 Exploring the Electric Vehicle revolution through interactive data storytelling

[![Made with Tableau](https://img.shields.io/badge/Made%20with-Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://www.tableau.com/)
[![Python](https://img.shields.io/badge/Worksheets-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![Dashboards](https://img.shields.io/badge/Scripts-30%2B-27AE60?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/Use-Educational-8E44AD?style=for-the-badge)](#-license)

</div>

---

## 📌 Overview

An **Electric Vehicle (EV) analytics** project. Original insights were built in Tableau; worksheets are now available as **Python code** (pandas + matplotlib/seaborn) that recreate each chart from CSV data.

> 🎯 **Goal:** Turn raw EV data into clear insights on pricing, performance, market segments, and charging infrastructure.

---

## 📂 Project Structure

```text
Data_Analytics/
├── README.md
├── requirements.txt
├── Data/
│   ├── ElectricCarData_Clean.csv
│   └── EVIndia.csv
└── Worksheets/
    ├── utils.py                      ← shared data loaders
    ├── 01_Pricing/                   (5 .py scripts)
    ├── 02_Performance/               (6 .py scripts)
    ├── 03_Market_Segments/           (8 .py scripts)
    ├── 04_Charging_Infrastructure/   (7 .py scripts)
    ├── 05_Summary_Cards/             (3 .py scripts)
    └── 06_Story/                     (1 .py script)
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt

# Example — Average Price by Brand
python Worksheets/01_Pricing/01_Average_Price_by_Brand.py

# Example — Story walkthrough
python Worksheets/06_Story/01_Scenes_of_Story.py
```

---

## 🗃️ Data Sources

| Source | Rows | File |
|--------|:----:|------|
| `ElectricCarData_Clean` | 103 | [`Data/ElectricCarData_Clean.csv`](Data/ElectricCarData_Clean.csv) |
| `EVIndia` | 12 | [`Data/EVIndia.csv`](Data/EVIndia.csv) |
| Charging stations | sample | Generated in `Worksheets/utils.py` |

---

## 📑 Worksheets (Python Code)

### 💰 Pricing
| Script | Description |
|--------|-------------|
| [`01_Average_Price_by_Brand.py`](Worksheets/01_Pricing/01_Average_Price_by_Brand.py) | Avg price (€) by brand |
| [`02_Price_vs_Range.py`](Worksheets/01_Pricing/02_Price_vs_Range.py) | Scatter: price vs range |
| [`03_Cheapest_Cars.py`](Worksheets/01_Pricing/03_Cheapest_Cars.py) | Top 10 cheapest EVs |
| [`04_Price_by_Car.py`](Worksheets/01_Pricing/04_Price_by_Car.py) | India EV prices (Lakhs) |
| [`05_PricevsRange.py`](Worksheets/01_Pricing/05_PricevsRange.py) | Price vs range with trend |

### ⚙️ Performance
| Script | Description |
|--------|-------------|
| [`01_Top_Speed.py`](Worksheets/02_Performance/01_Top_Speed.py) | Fastest 15 models |
| [`02_Top_Speed_by_Brand.py`](Worksheets/02_Performance/02_Top_Speed_by_Brand.py) | Max top speed by brand |
| [`03_Range_Comparison.py`](Worksheets/02_Performance/03_Range_Comparison.py) | India EV range |
| [`04_Range_vs_Efficiency.py`](Worksheets/02_Performance/04_Range_vs_Efficiency.py) | Range vs Wh/Km |
| [`05_Efficiency.py`](Worksheets/02_Performance/05_Efficiency.py) | Most efficient models |
| [`06_Fast_Charging.py`](Worksheets/02_Performance/06_Fast_Charging.py) | Fast-charge leaders |

### 🏷️ Market & Segments
| Script | Description |
|--------|-------------|
| [`01_Number_of_Models_by_Brand.py`](Worksheets/03_Market_Segments/01_Number_of_Models_by_Brand.py) | Model count by brand |
| [`02_Segment_Distribution.py`](Worksheets/03_Market_Segments/02_Segment_Distribution.py) | Segment pie chart |
| [`03_Brand_by_BodyStyle.py`](Worksheets/03_Market_Segments/03_Brand_by_BodyStyle.py) | Brand × body style |
| [`04_Brand_by_PowerTrain.py`](Worksheets/03_Market_Segments/04_Brand_by_PowerTrain.py) | Brand × powertrain |
| [`05_Drive_Type.py`](Worksheets/03_Market_Segments/05_Drive_Type.py) | Drive type mix |
| [`06_Different_EV_Cars.py`](Worksheets/03_Market_Segments/06_Different_EV_Cars.py) | India EV catalogue |
| [`07_Boot_Space.py`](Worksheets/03_Market_Segments/07_Boot_Space.py) | Boot space comparison |
| [`08_Top_10_Most_Efficient_EV_Brands.py`](Worksheets/03_Market_Segments/08_Top_10_Most_Efficient_EV_Brands.py) | Top efficient brands |

### 🔌 Charging Infrastructure
| Script | Description |
|--------|-------------|
| [`01_EV_Charging_Stations_Map.py`](Worksheets/04_Charging_Infrastructure/01_EV_Charging_Stations_Map.py) | Station map |
| [`02_Charging_Stations_by_Region.py`](Worksheets/04_Charging_Infrastructure/02_Charging_Stations_by_Region.py) | Stations by region |
| [`03_Charging_Stations_by_Charger_Type.py`](Worksheets/04_Charging_Infrastructure/03_Charging_Stations_by_Charger_Type.py) | By charger type |
| [`04_Charger_Type_by_Region.py`](Worksheets/04_Charging_Infrastructure/04_Charger_Type_by_Region.py) | Type mix per region |
| [`05_Charging_Power_Distribution.py`](Worksheets/04_Charging_Infrastructure/05_Charging_Power_Distribution.py) | Power histogram |
| [`06_Top_Regions_by_Charging_Stations.py`](Worksheets/04_Charging_Infrastructure/06_Top_Regions_by_Charging_Stations.py) | Top regions |
| [`07_Self_Service_Analysis.py`](Worksheets/04_Charging_Infrastructure/07_Self_Service_Analysis.py) | Printable exploration |

### 📊 Summary Cards & Story
| Script | Description |
|--------|-------------|
| [`01_Global_Summary_Card.py`](Worksheets/05_Summary_Cards/01_Global_Summary_Card.py) | Global KPIs |
| [`02_Charging_Summary_Card.py`](Worksheets/05_Summary_Cards/02_Charging_Summary_Card.py) | Charging KPIs |
| [`03_Total_Models.py`](Worksheets/05_Summary_Cards/03_Total_Models.py) | Total model count |
| [`01_Scenes_of_Story.py`](Worksheets/06_Story/01_Scenes_of_Story.py) | Guided insight story |

---

## 📜 License

For **educational** and **portfolio** use.
