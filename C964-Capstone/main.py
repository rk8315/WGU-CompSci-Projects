#region Environment Setup

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt
import numpy as np

#endregion Environment Setup

#region Data Preparation

# Load  and preview dataset
energy_data = pd.read_csv("PJME_hourly.csv", parse_dates=['Datetime'], index_col='Datetime')
data_set_preview = energy_data.head()
print("---Preview of the Energy Consumption dataset for PJME---")
print(data_set_preview)

# Handle missing values by filling it with a mean value of data
energy_data['PJME_MW'].fillna(energy_data['PJME_MW'].mean())

# Extract additional features from Datetime and preview
energy_data['hour'] = energy_data.index.hour
energy_data['day'] = energy_data.index.day
energy_data['month'] = energy_data.index.month
energy_data['year'] = energy_data.index.year

data_set_datetime_preview = energy_data.head()
print("---Preview of the Energy Consumption dataset for PJME with Datetime features---")
print(data_set_datetime_preview)

# Split data into features and targets
x = energy_data[['hour', 'day', 'month', 'year']] #features dataframe of datetime
y = energy_data['PJME_MW']       #target series of est. megawatts

# Split into training and testing sets
# 20% into test set, 80% into training set. Set seed to 10 for consistency
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)

#endregion Data Preparation 

#region Model Creation and Training

rfr_model = RandomForestRegressor(random_state=10)
rfr_model.fit(x_train, y_train)

y_pred = rfr_model.predict(x_test)

#endregion Model Creation and Training

#region Model Evaluation

min_MW = energy_data['PJME_MW'].min()
max_MW = energy_data['PJME_MW'].max()
mae = round(mean_absolute_error(y_test, y_pred), 2)
rmse = round(sqrt(mean_squared_error(y_test, y_pred)),2) 
mae_min_percent = round((mae / min_MW) * 100, 2)
mae_max_percent = round((mae / max_MW) * 100, 2)
rmse_min_percent = round((rmse / min_MW) * 100, 2)
rmse_max_percent = round((rmse / max_MW) * 100, 2)

print(f"Minimum MW: {min_MW}")
print(f"Maximum MW: {max_MW}")
print(f"Mean Absolute Error (MAE): {mae}. Percentage error: {mae_max_percent}% - {mae_min_percent}%")
print(f"Root Mean Squared Error (RMSE): {rmse}. Percentage error: {rmse_max_percent}% - {rmse_min_percent}%")

#endregion Model Evaluation

#region Visualize Existing Data

#endregion Visualize Existing Data

#region Forecast Energy Consumption

#endregion Forecast Energy Consumption

#region Visualize Forecast Data

#endregion Visualize Forecast Data