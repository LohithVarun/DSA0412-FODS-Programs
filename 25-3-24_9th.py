import matplotlib.pyplot as plt

weather_data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'temperature': [15.5, 17.2, 20.1, 22.8, 26.4, 28.9, 31.2, 30.7, 27.5, 23.6, 19.3, 16.8],
    'rainfall': [45.2, 32.1, 28.7, 19.5, 12.8, 7.2, 4.1, 6.3, 11.9, 25.7, 39.4, 51.6]
}

months = weather_data['month']
temperatures = weather_data['temperature']

plt.figure(figsize=(10, 6))
plt.plot(months, temperatures, marker='o')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature Data')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

rainfall_values = weather_data['rainfall']

plt.figure(figsize=(10, 6))
plt.scatter(months, rainfall_values)
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall Data')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
