# src/preprocessing.py
# Inline preprocessing examples (no custom def functions).
import os, gc, warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd

print("Preprocessing starter — running inline. Adjust paths as needed.")

RAW_PATH = os.path.join("data", "US_Accidents.csv")
if not os.path.exists(RAW_PATH):
    print(f"ERROR: dataset not found at {RAW_PATH}. Place the CSV there and rename to US_Accidents.csv")
else:
    data_df = pd.read_csv(RAW_PATH, low_memory=False)
    print("Loaded rows:", len(data_df))
    data_df.columns = [c.strip() for c in data_df.columns]
    if "Start_Time" in data_df.columns:
        data_df["Start_Time"] = pd.to_datetime(data_df["Start_Time"], errors="coerce")
        data_df["start_hour"] = data_df["Start_Time"].dt.hour
        data_df["start_dayofweek"] = data_df["Start_Time"].dt.dayofweek
    if "Severity" not in data_df.columns:
        print("WARNING: 'Severity' not found. You must provide a severity target for classification.")
    gc.collect()
