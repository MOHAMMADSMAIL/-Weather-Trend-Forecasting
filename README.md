
# Weather Trend Forecasting 🌦️

## Project Overview

This project focuses on analyzing weather data and forecasting future temperature trends using data science techniques.

The project uses the **Global Weather Repository Dataset** and applies a complete machine learning workflow including:

* Data cleaning and preprocessing.
* Exploratory Data Analysis (EDA).
* Time series forecasting.
* Model evaluation.
* Anomaly detection.

The main objective is to predict daily temperature trends using historical weather observations.

---

## Dataset

Dataset:

**Global Weather Repository**

The dataset contains daily weather information from cities around the world with more than 40 features.

For this project:

* Location: **Amman, Jordan**
* Target variable: **temperature_celsius**
* Time feature: **last_updated**

Selected features:

* location_name
* last_updated
* temperature_celsius

---

## Project Structure

```
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
│   └── Weather_Trend_Forecasting_Report.md
│
├── requirements.txt
└── README.md
```

---

## Methodology

### 1. Data Preprocessing

The preprocessing steps included:

* Loading the dataset.
* Converting `last_updated` into datetime format.
* Checking missing values.
* Filtering Amman weather data.
* Aggregating observations into daily temperature averages.
* Splitting data into training and testing sets without shuffle.

---

### 2. Exploratory Data Analysis

EDA was performed to analyze:

* Temperature trends over time.
* Precipitation patterns.
* Weather feature relationships.

Visualizations were created to understand historical weather behavior.

---

### 3. Forecasting Models

The following models were implemented:

### Baseline Model

A Naive forecasting model was created as a simple reference.

### SARIMA Model

A Seasonal ARIMA model was used for time series forecasting.

Configuration:

```
SARIMAX(1,1,1)x(1,1,1,7)
```

The model captures temporal patterns and weekly seasonality.

### Random Forest Model

A machine learning approach was implemented using lag features:

* Previous day temperature.
* Previous 7 days temperature.

---

## Evaluation Metrics

The models were evaluated using:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)

Models were compared based on forecasting error.

---

## Advanced Analysis

### Anomaly Detection

Temperature anomalies were detected using the Z-score method.

Threshold:

```
|Z-score| > 3
```

The analysis was used to identify unusual temperature observations.

---

## Results

The project successfully demonstrates:

* Weather data preprocessing.
* Time series forecasting.
* Model comparison.
* Weather trend analysis.
* Anomaly detection.

Detailed results and analysis are available in:

[Weather Trend Forecasting Report](reports/Weather_Trend_Forecasting_Report.md)

---

## Installation and Running

Clone the repository:

```bash
git clone https://github.com/MOHAMMADSMAIL/-Weather-Trend-Forecasting.git
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Jupyter Notebook:

```bash
jupyter notebook
```

---

## Libraries Used

Main libraries:

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Statsmodels
* SciPy

---

## Future Improvements

Future work may include:

* Adding more cities for global forecasting.
* Using additional weather features.
* Testing advanced models such as XGBoost and LSTM.
* Creating an interactive weather dashboard.

---

## Author

Mohammad Al-Louzi

Artificial Intelligence Student
