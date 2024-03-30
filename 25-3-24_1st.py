import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

weather_data = {
    'Date': pd.date_range(start='2018-01-01', end='2022-12-31', freq='D'),
    'Temperature': np.random.uniform(low=-10, high=40, size=1826),
    'Precipitation': np.random.exponential(scale=2, size=1826),
    'Wind_Speed': np.random.uniform(low=0, high=20, size=1826),
    'Humidity': np.random.uniform(low=20, high=100, size=1826)
}

df = pd.DataFrame(weather_data)

df['Season'] = df['Date'].dt.quarter
df['Year'] = df['Date'].dt.year

season_temp = df.groupby('Season')['Temperature'].mean().reset_index()
plt.figure(figsize=(8, 6))
plt.bar(season_temp['Season'], season_temp['Temperature'])
plt.xlabel('Season')
plt.ylabel('Average Temperature (°C)')
plt.title('Average Temperature Trends by Season')
plt.show()

precipitation_trend = df.groupby(pd.Grouper(key='Date', freq='M'))['Precipitation'].sum().reset_index()
precipitation_trend['Month'] = pd.to_datetime(precipitation_trend['Date']).dt.month
plt.figure(figsize=(12, 6))
plt.plot(precipitation_trend['Date'], precipitation_trend['Precipitation'])
plt.xlabel('Date')
plt.ylabel('Total Precipitation (mm)')
plt.title('Monthly Precipitation Trend')
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(df['Temperature'], bins=30, edgecolor='black')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.title('Temperature Distribution')
plt.axvline(df['Temperature'].mean(), color='r', linestyle='--', label='Mean')
plt.axvline(df['Temperature'].quantile(0.05), color='g', linestyle='--', label='5th Percentile')
plt.axvline(df['Temperature'].quantile(0.95), color='g', linestyle='--', label='95th Percentile')
plt.legend()
plt.show()
