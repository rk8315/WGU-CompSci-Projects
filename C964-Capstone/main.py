#region Environment Setup

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt

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

# Create subplots for graphing
fig, axes = plt.subplots(2, 2, figsize=(14, 10), layout="constrained")

# lineplot
sns.lineplot(ax=axes[0,0], x=energy_data.index, y='PJME_MW', data=energy_data)
axes[0,0].set_title("Historical Energy Consumption Over Time (PJME)")
axes[0,0].set_xlabel("Date")
axes[0,0].set_ylabel("Energy Consumption (MW)")

# Heatmap
pivot_table = energy_data.pivot_table(values='PJME_MW', index='hour', columns='day', aggfunc='mean')
sns.heatmap(ax=axes[0,1], data=pivot_table, cmap='viridis')
axes[0,1].set_title("Average Energy Consumption by Hour and Day (PJME)")
axes[0,1].set_xlabel("Day")
axes[0,1].set_ylabel("Hour")

# Boxplot
sns.boxplot(ax=axes[1,0], x='month', y='PJME_MW', data=energy_data)
axes[1,0].set_title("Distribution of Energy Consumption - Monthly (PJME)")
axes[1,0].set_xlabel("Month")
axes[1,0].set_ylabel("Energy Consumption (MW)")

# Scatterplot
sns.scatterplot(ax=axes[1,1], x='hour', y='PJME_MW', data=energy_data, alpha=0.5)
axes[1,1].set_title("Energy Consumption - Hourly (PJME)")
axes[1,1].set_xlabel("Hour")
axes[1,1].set_ylabel("Energy Consumption (MW)")

plt.show()

#endregion Visualize Existing Data

#region Forecast Energy Consumption

date_selection = "09/15/2024"
date_selected = date_selection.split("/")

#24 hours of a future date
forecast_energy_data = pd.DataFrame({
    'hour': [i for i in range(24)],
    'day': [date_selected[1]]*24,
    'month': [date_selected[0]]*24,
    'year': [date_selected[2]]*24
})

forecast_energy_model = rfr_model.predict(forecast_energy_data)

forecast_energy_data['PJME_MW'] = forecast_energy_model

print(f"Forecast data: {forecast_energy_data}")

#endregion Forecast Energy Consumption

#region Visualize Forecast Data

plt.figure(figsize=(14, 10))
sns.lineplot(x=forecast_energy_data.index, y=forecast_energy_data['PJME_MW'])
plt.title(f"Energy Consumption Forecast for Date: {date_selection}")
plt.xlabel("Hour")
plt.ylabel("Energy Consumption (MW)")

plt.show()

#endregion Visualize Forecast Data