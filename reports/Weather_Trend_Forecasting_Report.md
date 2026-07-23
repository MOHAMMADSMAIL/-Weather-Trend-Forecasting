Weather-Trend-Forecasting
│
├── reports
│   └── Weather_Trend_Forecasting_Report.md
│
├── notebooks
│   ├── 01_data_exploration.ipynb
│   └── 02_model_building.ipynb
│
├── data
│   └── GlobalWeatherRepository.csv
│
├── README.md
└── requirements.txt



# Weather Trend Forecasting Report

## 1. Project Overview and Objective

Weather forecasting is an important application of data science that helps understand weather behavior and predict future conditions.

The objective of this project is to analyze the **Global Weather Repository** dataset and build a forecasting system to predict future temperature trends.

The project workflow includes:

* Data cleaning and preprocessing.
* Exploratory Data Analysis (EDA).
* Time series preparation.
* Building forecasting models.
* Evaluating model performance.
* Detecting unusual temperature observations.

The main prediction target in this project is:

**Daily Temperature (°C)**

The analysis was performed using weather data for:

**Amman, Jordan**

The main time feature used for analysis was:

`last_updated`

---

# 2. Dataset Description

The dataset used in this project is:

**Global Weather Repository Dataset**

The dataset contains daily weather information for cities around the world and includes more than 40 weather-related features.

Examples of features:

* Location information
* Country
* Latitude and Longitude
* Date and time information
* Temperature
* Precipitation
* Humidity
* Wind speed
* Pressure
* Cloud coverage
* Air quality measurements

For this project, the following columns were selected:

| Column              | Description                  |
| ------------------- | ---------------------------- |
| location_name       | City name                    |
| last_updated        | Weather observation date     |
| temperature_celsius | Temperature value in Celsius |

The selected city for forecasting:

**Amman, Jordan**

---

# 3. Data Cleaning and Preprocessing

## 3.1 Data Loading

The dataset was loaded using the Pandas library.

The `last_updated` column was converted into datetime format to support time series analysis.

---

## 3.2 Missing Values

The dataset was checked for missing values.

No missing values were found in the selected columns.

---

## 3.3 Data Filtering

The dataset was filtered to include only weather observations from Amman.

The data was sorted according to the date column:

`last_updated`

to maintain chronological order.

---

## 3.4 Daily Temperature Aggregation

The original dataset contains weather observations that were transformed into daily data.

The daily average temperature was calculated using:

* Daily resampling (`resample("D")`)
* Mean temperature calculation

---

## 3.5 Handling Missing Days

Missing dates in the time series were handled using forward filling:

`ffill()`

This keeps the time series continuous and suitable for forecasting.

---

## 3.6 Train/Test Split

The dataset was divided chronologically:

* 80% Training data
* 20% Testing data

No shuffle operation was used because time series data depends on the order of observations.

---

# 4. Exploratory Data Analysis (EDA)

EDA was performed to understand temperature behavior and weather patterns.

## 4.1 Temperature Trend

A time series plot was created to visualize temperature changes over time.

The visualization shows:

* Daily temperature variations.
* Seasonal behavior.
* Temperature fluctuations.

---

## 4.2 Precipitation Analysis

Precipitation data was analyzed and visualized to understand rainfall patterns.

---

## 4.3 Correlation Analysis

Correlation analysis was performed to understand relationships between weather variables.

This helps identify important features and possible dependencies.

---

# 5. Forecasting Models

Two forecasting approaches were implemented and compared.

---

# 5.1 Baseline Model (Naive Forecast)

A simple baseline model was created as a reference.

The model uses the previous temperature value as the prediction for the next observation.

The purpose of this model is to provide a basic comparison before using more advanced methods.

---

# 5.2 SARIMA Forecasting Model

The main time series forecasting model used was:

**SARIMA (Seasonal AutoRegressive Integrated Moving Average)**

The implemented model:

```
SARIMAX(1,1,1)x(1,1,1,7)
```

The seasonal period was set to 7 days to capture weekly patterns.

The model was trained using the training dataset and used to forecast future temperatures during the testing period.

---

# 5.3 Random Forest Forecasting Model

A machine learning forecasting approach was also implemented.

Lag features were created:

* Previous day temperature (`lag_1`)
* Previous 7 days temperature (`lag_7`)

A Random Forest Regressor model was trained using these features.

This allowed comparison between:

* Traditional time series forecasting.
* Machine learning forecasting.

---

# 6. Model Evaluation

The models were evaluated using:

## Mean Absolute Error (MAE)

MAE measures the average difference between predicted and actual values.

## Root Mean Squared Error (RMSE)

RMSE measures prediction error and gives higher importance to larger errors.

The models were compared based on their error values.

Example comparison:

| Model         | MAE              | RMSE             |
| ------------- | ---------------- | ---------------- |
| SARIMA        | Calculated value | Calculated value |
| Random Forest | Calculated value | Calculated value |

The model with lower MAE and RMSE provides better forecasting performance.

---

# 7. Actual vs Predicted Visualization

A comparison visualization was created between:

* Actual temperature values.
* SARIMA predicted temperature values.

This plot shows how closely the model follows the real temperature trend during the test period.

---

# 8. Advanced Analysis: Anomaly Detection

Anomaly detection was performed using the **Z-score method**.

The purpose was to detect unusual temperature observations.

The threshold used:

```
|Z-score| > 3
```

Values above this threshold are considered possible anomalies.

The result:

```
Number of anomalies: 0
```

This indicates that no extreme temperature observations were detected during the analyzed period.

---

# 9. Results and Insights

The project provided several insights:

* Temperature values followed normal seasonal variations.
* Time series models can capture historical temperature behavior.
* SARIMA was able to model temporal dependencies.
* Random Forest provided a machine learning comparison using historical temperature patterns.
* No significant temperature anomalies were found.

---

# 10. Limitations

This project has some limitations:

* The analysis focused on one city only.
* Only temperature was selected as the prediction target.
* More weather features could improve forecasting accuracy.
* Advanced deep learning models were not implemented.

---

# 11. Future Improvements

Possible improvements:

* Add more cities and perform global forecasting.
* Include humidity, wind, and precipitation features.
* Test advanced models such as XGBoost, LSTM, or Transformers.
* Build an interactive dashboard for weather analysis.

---

# 12. Conclusion

This project demonstrates a complete data science workflow:

* Data preprocessing.
* Exploratory data analysis.
* Time series forecasting.
* Machine learning comparison.
* Model evaluation.
* Anomaly detection.

The developed forecasting pipeline provides a foundation for future improvements in weather prediction systems.
