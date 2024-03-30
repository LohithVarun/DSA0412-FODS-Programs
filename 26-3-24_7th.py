import numpy as np
import matplotlib.pyplot as plt

time_spent = [8, 12, 5, 15, 10, 20, 7, 18, 25, 8, 12, 22, 15, 10, 30, 7, 18, 15, 20, 12]

median_time = np.median(time_spent)

q1 = np.percentile(time_spent, 25)
q3 = np.percentile(time_spent, 75)
iqr = q3 - q1

plt.figure(figsize=(8, 6))
plt.boxplot(time_spent, patch_artist=True)
plt.title("Distribution of Time Spent on Website")
plt.xlabel("Time Spent (minutes)")
plt.show()

print(f"Median time spent: {median_time} minutes")
print(f"Interquartile range (IQR): {iqr} minutes")
