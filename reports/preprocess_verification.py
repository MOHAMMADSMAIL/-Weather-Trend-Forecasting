from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

project_root = Path.cwd()
data_path = project_root / "data" / "GlobalWeatherRepository.csv"
if not data_path.exists():
    data_path = project_root / ".." / "data" / "GlobalWeatherRepository.csv"

raw_df = pd.read_csv(data_path)
df = raw_df.copy()

print("Rows before cleaning:", df.shape[0])
print("Columns before cleaning:", df.shape[1])
print("\nFirst rows:")
print(df.head(3))
print("\nColumns:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)

# Convert the timestamp column into datetime format.
df["last_updated"] = pd.to_datetime(df["last_updated"], errors="coerce")

print("Missing values after datetime conversion:")
print(df.isnull().sum())

invalid_value_columns = [
    "temperature_celsius",
    "pressure_mb",
    "wind_kph",
    "precip_mm",
    "humidity",
    "cloud",
    "visibility_km",
    "uv_index",
    "air_quality_Carbon_Monoxide",
    "air_quality_Sulphur_dioxide",
    "air_quality_PM10",
]
for col in invalid_value_columns:
    if col in df.columns:
        df[col] = df[col].replace(-9999, np.nan)

print("Missing values after invalid value replacement:")
print(df[invalid_value_columns].isnull().sum())

outlier_features = ["temperature_celsius", "pressure_mb", "wind_kph", "precip_mm"]
outlier_summary = {}
for col in outlier_features:
    if col in df.columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        mask = (df[col] < lower_bound) | (df[col] > upper_bound)
        outlier_summary[col] = int(mask.sum())
        df.loc[mask, col] = np.nan

print("Outliers replaced with NaN:")
print(outlier_summary)
print("\nMissing values after outlier treatment:")
print(df[outlier_features].isnull().sum())

numeric_columns = [
    "latitude",
    "longitude",
    "humidity",
    "pressure_mb",
    "wind_kph",
    "precip_mm",
    "cloud",
    "visibility_km",
    "uv_index",
    "temperature_celsius",
]
for col in numeric_columns:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

df["year"] = df["last_updated"].dt.year
df["month"] = df["last_updated"].dt.month
df["day"] = df["last_updated"].dt.day
df["hour"] = df["last_updated"].dt.hour

print("Missing values after imputation:")
print(df[numeric_columns + ["year", "month", "day", "hour"]].isnull().sum())
print("\nTime feature preview:")
print(df[["last_updated", "year", "month", "day", "hour"]].head())

model_features = [
    "latitude",
    "longitude",
    "month",
    "day",
    "hour",
    "humidity",
    "pressure_mb",
    "wind_kph",
    "precip_mm",
    "cloud",
    "visibility_km",
    "uv_index",
]
target_col = "temperature_celsius"
processed_df = df[model_features + [target_col]].copy()

print("Processed dataframe shape:", processed_df.shape)
print("\nProcessed dataframe preview:")
print(processed_df.head())

scaler = StandardScaler()
processed_df[model_features] = scaler.fit_transform(processed_df[model_features])

print("Scaled dataframe preview:")
print(processed_df.head())
print("\nFeature means after scaling:")
print(processed_df[model_features].mean().round(4))
print("\nFeature standard deviations after scaling:")
print(processed_df[model_features].std().round(4))
