#region Environment Setup
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
import numpy as np
#endregion Environment Setup

#region Data Preparation
# Load  and preview dataset
energy_data = pd.read_csv("PJME_hourly.csv", parse_dates=['Datetime'], index_col='Datetime')
data_set_test = energy_data.head()
print(data_set_test)

# Handle missing values by filling it with a mean value of data
energy_data['PJME_MW'].fillna(energy_data['PJME_MW'].mean())

# Extract additional features from Datetime and preview
energy_data['hour'] = energy_data.index.hour
energy_data['day'] = energy_data.index.day
energy_data['month'] = energy_data.index.month
energy_data['year'] = energy_data.index.year

data_set_datetime_test = energy_data.head()
print(data_set_datetime_test)

# Split data into features and targets
x = energy_data['hour', 'day', 'month', 'year'] #features dataframe
y = energy_data['PJME_MW']       #target series

# Split into training and testing sets
# 20% into test set, 80% into training set. Set seed to 10 for consistency
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=10)

#endregion Data Preparation 