from collections import Counter

weather_data = [
    ("sunny", 85),
    ("cloudy", 62),
    ("rainy", 40),
    ("windy", 28),
    ("snowy", 15),
    ("foggy", 20),
    ("thunderstorm", 10),
    ("sunny", 90),
    ("rainy", 35),
    ("cloudy", 55),
]

weather_freq = Counter(condition for condition, occurrences in weather_data for _ in range(occurrences))

print("Frequency Distribution of Weather Conditions:")
for condition, freq in weather_freq.most_common():
    print(f"{condition}: {freq} occurrences")

most_common_weather = max(weather_freq, key=weather_freq.get)
print(f"\nThe most common weather type is '{most_common_weather}'.")
