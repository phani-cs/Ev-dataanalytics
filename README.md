<div align="center">

# ⚡ EV Data Analytics

### Interactive EV website · 4 datasets · pricing · performance · charging

[![Streamlit](https://img.shields.io/badge/App-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](#-run-as-a-website)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![Datasets](https://img.shields.io/badge/Datasets-4-27AE60?style=for-the-badge)](#-datasets)
[![License](https://img.shields.io/badge/Use-Educational-8E44AD?style=for-the-badge)](#-license)

</div>

---

## Overview

Electric Vehicle analytics with **all 4 source datasets**, worksheet Python scripts, and a **Streamlit website** you can run locally and publish online.

---

## Project structure

```text
Data_Analytics/
├── app.py                          ← website entry point
├── requirements.txt
├── README.md
├── .streamlit/config.toml
├── Data/                           ← all 4 datasets
│   ├── ElectricCarData_Clean.csv
│   ├── EVIndia.csv
│   ├── Cheapestelectriccars-EVDatabase.csv
│   └── electric_vehicle_charging_station_list.csv
└── Worksheets/                     ← Python chart scripts
    ├── utils.py
    ├── 01_Pricing/
    ├── 02_Performance/
    ├── 03_Market_Segments/
    ├── 04_Charging_Infrastructure/
    ├── 05_Summary_Cards/
    └── 06_Story/
```

---

## Datasets (4)

| # | File | Rows | What it covers |
|---|------|:----:|----------------|
| 1 | [`Data/ElectricCarData_Clean.csv`](Data/ElectricCarData_Clean.csv) | 103 | Global EV specs — brand, price (€), range, efficiency, powertrain |
| 2 | [`Data/EVIndia.csv`](Data/EVIndia.csv) | 12 | India EVs — price (Lakhs), range, boot space |
| 3 | [`Data/Cheapestelectriccars-EVDatabase.csv`](Data/Cheapestelectriccars-EVDatabase.csv) | ~180 | Cheapest EV DB — UK/Germany price, drive, top speed, fast charge |
| 4 | [`Data/electric_vehicle_charging_station_list.csv`](Data/electric_vehicle_charging_station_list.csv) | 50 | India charging stations — region, charger type, power, map coords |

Open the **Datasets** page in the website to browse all four tables.

---

## How to run

1. Copy project folder to other laptop (`Data_Analytics` / `Ev-dataanalytics`)

2. Install software
   - Python 3.10+ (recommended 3.12)
   - During install, tick **Add Python to PATH**

3. Open terminal in project folder

```bash
cd path\to\Data_Analytics
```

4. Install Python packages once

```bash
python -m pip install -r requirements.txt
```

5. Run app

```bash
python -m streamlit run app.py
```

6. Open in browser

```text
http://localhost:8501
```

### If error comes

- **Python not found**  
  Install Python and add to PATH. Or use full path:

```bash
"%LOCALAPPDATA%\Programs\Python\Python312\python.exe" -m streamlit run app.py
```

- **streamlit not recognized**  
  Install again:

```bash
python -m pip install streamlit plotly pandas
```

- **ModuleNotFoundError**  
  Reinstall requirements:

```bash
python -m pip install -r requirements.txt
```

---

## Publish online (Streamlit Cloud — free)

1. Push this repo to GitHub (`https://github.com/phani-cs/Ev-dataanalytics`)
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **New app**
4. Choose repo `phani-cs/Ev-dataanalytics`, branch `main`, main file `app.py`
5. Click **Deploy**

---

## License

For educational and portfolio use.
