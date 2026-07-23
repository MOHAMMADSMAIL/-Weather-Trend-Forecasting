
# Weather Trend Forecasting

## Project Overview

This project focuses on analyzing global weather data and forecasting future temperature trends using data science and machine learning techniques.

The project uses the **Global Weather Repository Dataset** from Kaggle and applies a complete data science workflow including:

* Data cleaning and preprocessing.
* Exploratory Data Analysis (EDA).
* Time series preparation.
* Forecasting model development.
* Model evaluation.
* Anomaly detection.
* Machine learning model comparison.

The main objective is to analyze historical weather observations and build a forecasting pipeline to predict future temperature trends.

---

## Dataset

### Global Weather Repository Dataset

The dataset contains daily weather information for cities around the world with more than 40 weather-related features.

For this project:

* **Selected Location:** Amman, Jordan
* **Prediction Target:** `temperature_celsius`
* **Time Feature:** `last_updated`

---

## Project Structure

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
├── requirements.txt
└── README.md
```

---

## Methodology

### 1. Data Preprocessing

The preprocessing pipeline includes:

* Loading the dataset using Pandas.
* Converting `last_updated` into datetime format.
* Checking missing values.
* Handling invalid values.
* Detecting and treating outliers using the IQR method.
* Filtering weather observations for Amman, Jordan.
* Aggregating observations into daily temperature values.
* Creating time-based features.
* Scaling features using StandardScaler.
* Splitting data into training and testing datasets without shuffling.

---

## Data Preprocessing Verification

A preprocessing verification script was created to validate the data preparation pipeline.

The script performs:

* Dataset loading and inspection.
* Datetime conversion for `last_updated`.
* Invalid value handling.
* Missing value detection and imputation.
* Outlier detection using the IQR method.
* Feature extraction from timestamps.
* Feature selection for modeling.
* Feature scaling using StandardScaler.

The preprocessing script is available at:

```text
reports/preprocess_verification.py
```

This verification step confirms that the preprocessing workflow is reproducible outside the notebook and can be reviewed directly from the project files.

---

## 2. Exploratory Data Analysis (EDA)

EDA was performed to understand weather behavior and identify important patterns.

The analysis includes:

### Temperature Analysis

Visualizing temperature changes over time to identify:

* Seasonal trends.
* Temperature fluctuations.
* Long-term behavior.

### Precipitation Analysis

Analyzing precipitation patterns and rainfall variations.

### Correlation Analysis

Studying relationships between weather variables using correlation analysis.

Visualizations were created using:

* Matplotlib
* Seaborn

---

## 3. Forecasting Models

Multiple forecasting approaches were implemented.

### Baseline Model

A Naive Forecasting model was created as a simple reference.

The model predicts future temperature using previous observations.

### SARIMA Model

A Seasonal ARIMA forecasting model was implemented using:

```text
SARIMAX(1,1,1)x(1,1,1,7)
```

The model captures historical temperature patterns, temporal dependencies, and weekly seasonal behavior.

### Random Forest Model

A machine learning forecasting model was implemented using lag features.

Created features:

* Previous day temperature (`lag_1`)
* Previous 7 days temperature (`lag_7`)

The model was trained using Random Forest Regressor.

---

## Model Evaluation

The models were evaluated using:

### MAE

Mean Absolute Error measures the average difference between predicted and actual values.

### RMSE

Root Mean Squared Error measures prediction error and gives higher importance to larger mistakes.

Evaluation results:

| Model         | MAE       | RMSE      |
| ------------- | --------- | --------- |
| SARIMA        | 11.841225 | 14.480171 |
| Random Forest | 2.220473  | 2.867336  |

Based on the evaluation results, the Random Forest model achieved lower MAE and RMSE than SARIMA, indicating better forecasting performance on the test data.

---

## Actual vs Predicted Visualization

A visualization was created comparing:

* Actual temperature values.
* SARIMA predicted temperature values.

The plot shows how accurately the model follows the real temperature trend during the testing period.

---

## Advanced Analysis

### Anomaly Detection

Temperature anomaly detection was performed using the Z-score method.

Threshold:

```text
|Z-score| > 3
```

Values outside this range are considered possible abnormal observations.

---

## Results

The project successfully demonstrates a complete weather forecasting workflow:

* Data preprocessing.
* Exploratory analysis.
* Time series forecasting.
* Machine learning comparison.
* Model evaluation.
* Anomaly detection.

The detailed analysis is available in:

```text
reports/Weather_Trend_Forecasting_Report.md
```

---

## Installation and Running

### Clone Repository

```bash
git clone https://github.com/MOHAMMADSMAIL/-Weather-Trend-Forecasting.git
```

Move into project folder:

```bash
cd -Weather-Trend-Forecasting
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment on Windows:

```bash
venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Project

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/01_data_exploration.ipynb
notebooks/02_model_building.ipynb
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
* Jupyter Notebook

---

## Future Improvements

Possible future improvements:

* Add more cities for global forecasting.
* Include additional weather features.
* Test advanced models such as XGBoost, LSTM, or Transformers.
* Build an interactive weather dashboard.
* Deploy the forecasting model as a web application.

---

## Author

**Mohammad Al-Louzi**

Artificial Intelligence Student