
# Weather Trend Forecasting Report

## PM Accelerator Mission Statement

PM Accelerator focuses on developing technical and professional skills by providing education, mentorship, and practical opportunities. The organization helps individuals improve their abilities, connect with industry requirements, and build successful careers through real-world learning experiences.

---

# 1. Project Overview and Objective

Weather forecasting is an important application of data science that helps analyze historical weather patterns and predict future weather conditions.

The objective of this project is to analyze the **Global Weather Repository Dataset** and build a forecasting pipeline capable of predicting future temperature trends using time series analysis and machine learning techniques.

The project demonstrates a complete data science workflow including:

- Data cleaning and preprocessing.
- Exploratory Data Analysis (EDA).
- Feature engineering.
- Time series preparation.
- Forecasting model development.
- Model evaluation.
- Anomaly detection.

The main prediction target is:

**Daily Temperature (°C)**

The selected forecasting location:

**Amman, Jordan**

The main time feature used:

`last_updated`

---

# 2. Dataset Description

The dataset used in this project is:

**Global Weather Repository Dataset**

The dataset contains daily weather observations from cities around the world with more than 40 weather-related features.

The dataset includes:

- Location information.
- Country and city names.
- Latitude and longitude.
- Date and time information.
- Temperature measurements.
- Precipitation.
- Humidity.
- Wind speed.
- Atmospheric pressure.
- Cloud coverage.
- Visibility.
- Air quality measurements.

For this project, the main selected columns were:

| Column | Description |
|---|---|
| location_name | City name |
| last_updated | Weather observation timestamp |
| temperature_celsius | Temperature value in Celsius |
| precip_mm | Precipitation amount |

The forecasting analysis was performed on:

**Amman, Jordan**

---

# 3. Data Cleaning and Preprocessing

## 3.0 Preprocessing Verification Script

A preprocessing verification script was developed to validate the complete data preparation workflow.

The script performs the following operations:

- Loading and inspecting the original dataset.
- Checking dataset dimensions and data types.
- Converting `last_updated` into datetime format.
- Detecting invalid values such as `-9999`.
- Handling missing values using median imputation.
- Detecting and treating outliers using the IQR method.
- Extracting time-based features:
  - Year
  - Month
  - Day
  - Hour
- Selecting important model features.
- Applying StandardScaler normalization.

The script is available at:

```text
reports/preprocess_verification.py
```

This verification step improves data reliability and ensures that the dataset is prepared correctly before model training.

---

## 3.1 Data Loading

The dataset was loaded using the Pandas library.

A copy of the original dataset was created to preserve the raw data.

The data structure, columns, and data types were inspected before processing.

---

## 3.2 Datetime Conversion

The `last_updated` column was converted into datetime format.

This step was necessary because the project uses time series forecasting techniques.

Additional time features were extracted:

- Year
- Month
- Day
- Hour

These features help capture seasonal and temporal patterns.

---

## 3.3 Missing Values Handling

The dataset was checked for missing values.

Invalid values such as `-9999` were treated as missing values.

Missing numerical values were handled using median imputation to maintain data consistency.

---

## 3.4 Outlier Detection and Treatment

Outliers were analyzed using the IQR (Interquartile Range) method.

The following weather features were checked:

- Temperature.
- Pressure.
- Wind speed.
- Precipitation.

Detected extreme values were replaced with missing values and later handled through imputation.

---

## 3.5 Feature Scaling

Numerical features were normalized using:

**StandardScaler**

The scaling process was applied to model features to improve machine learning model performance.

---

## 3.6 Time Series Preparation

The weather observations were filtered for Amman.

The data was sorted chronologically using:

`last_updated`

Daily average temperature values were calculated using daily resampling.

Missing dates were handled using:

`ffill()`

to maintain continuous time series data.

---

## 3.7 Train/Test Split

The dataset was divided into:

- 80% Training data.
- 20% Testing data.

The split was performed without random shuffling because time series forecasting depends on chronological order.

---

# 4. Exploratory Data Analysis (EDA)

EDA was performed to understand weather behavior and identify important patterns.

---

## 4.1 Temperature Trend Analysis

A time series visualization was created to analyze temperature changes over time.

The analysis showed:

- Daily temperature fluctuations.
- Seasonal changes.
- Long-term temperature behavior.

---

## 4.2 Precipitation Analysis

Precipitation values were analyzed and visualized.

The analysis helped understand rainfall distribution and weather variations.

---

## 4.3 Correlation Analysis

Correlation analysis was performed between weather features.

A correlation heatmap was created to identify relationships between:

- Temperature.
- Humidity.
- Pressure.
- Wind.
- Precipitation.

---

# 5. Forecasting Models

Multiple forecasting approaches were implemented.

---

## 5.1 Naive Forecast Baseline Model

A simple baseline model was created.

The model predicts the next temperature value using the previous observation.

This provides a reference point to evaluate more advanced forecasting methods.

---

## 5.2 SARIMA Forecasting Model

The main time series model used was:

**SARIMA (Seasonal AutoRegressive Integrated Moving Average)**

Implementation:

```text
SARIMAX(1,1,1)x(1,1,1,7)
```

The seasonal period was set to 7 days to capture weekly temperature patterns.

The model was trained using historical temperature observations and used to predict future temperature values.

---

## 5.3 Random Forest Forecasting Model

A machine learning forecasting approach was implemented using:

**Random Forest Regressor**

Historical temperature values were transformed into lag features:

- Previous day temperature (`lag_1`)
- Previous 7 days temperature (`lag_7`)

The model learned relationships between previous weather observations and future temperature values.

---

# 6. Model Evaluation

The forecasting models were evaluated using:

## Mean Absolute Error (MAE)

MAE measures the average absolute difference between predicted and actual values.

Lower MAE indicates better performance.

---

## Root Mean Squared Error (RMSE)

RMSE measures prediction error while giving more importance to larger errors.

Lower RMSE indicates better forecasting accuracy.

---

## Model Comparison

| Model | MAE | RMSE |
|---|---:|---:|
| SARIMA | 11.841225 | 14.480171 |
| Random Forest | 2.220473 | 2.867336 |

The model with lower error values provides better forecasting performance.

Based on the evaluation results, the Random Forest model achieved lower MAE and RMSE than SARIMA.

---

# 7. Actual vs Predicted Visualization

A comparison visualization was created between:

- Actual temperature values.
- SARIMA predicted temperature values.

The visualization demonstrates how closely the forecasting model follows the real temperature trend during the testing period.

---

# 8. Advanced Analysis: Anomaly Detection

Anomaly detection was performed using the:

**Z-score Method**

The purpose was to identify unusual temperature observations.

The detection rule:

```text
|Z-score| > 3
```

Values outside this range were considered potential anomalies.

Result:

No extreme temperature observations were detected during the analyzed period.

---

# 9. Results and Insights

The project provided several important insights:

- Weather data can be successfully processed using a complete data science pipeline.
- Temperature showed seasonal and daily variations.
- SARIMA successfully modeled historical temperature patterns.
- Random Forest provided a machine learning comparison using lag features.
- No significant temperature anomalies were detected.
- Historical weather information can be used to forecast future temperature trends.

---

# 10. Limitations

The project has some limitations:

- The forecasting analysis focused on one city only.
- The target variable was limited to temperature.
- More weather features could improve prediction accuracy.
- Deep learning models were not implemented.

---

# 11. Future Improvements

Possible improvements include:

- Expanding forecasting to multiple cities.
- Adding more environmental features.
- Testing advanced models such as:
  - XGBoost.
  - LSTM.
  - Transformer-based models.
- Creating an interactive dashboard for weather analysis.
- Deploying the forecasting model as a web application.

---

# 12. Technologies Used

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- SciPy

## Development Tools

- Jupyter Notebook
- Python Virtual Environment (venv)
- GitHub

## Data Processing Techniques

The project applied:

- Datetime feature extraction.
- Missing value handling.
- IQR-based outlier detection.
- Median imputation.
- Feature normalization using StandardScaler.

---

# 13. Repository Structure

```text
Weather-Trend-Forecasting
│
├── data
│   └── GlobalWeatherRepository.csv
│
├── notebooks
│   ├── 01_data_exploration.ipynb
│   └── 02_model_building.ipynb
│
├── reports
│   ├── Weather_Trend_Forecasting_Report.md
│   └── preprocess_verification.py
│
├── README.md
└── requirements.txt
```
```