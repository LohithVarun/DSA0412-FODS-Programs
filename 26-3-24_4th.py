import numpy as np
import matplotlib.pyplot as plt

# Scores data
scores = [85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 5, 98, 72]

# Calculate mean
mean_score = np.mean(scores)

# Calculate median
median_score = np.median(scores)

# Sort the data for quartiles
sorted_scores = np.sort(scores)

# Calculate quartiles
q1 = np.percentile(sorted_scores, 25)
q3 = np.percentile(sorted_scores, 75)

# Identify outliers (1.5 IQR rule)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

outliers = [score for score in scores if score < lower_bound or score > upper_bound]

# Print results
print("Mean:", mean_score)
print("Median:", median_score)
print("Q1:", q1)
print("Q3:", q3)
print("Outliers:", outliers)

# Create box plot
plt.boxplot(scores)
plt.xlabel("Scores")
plt.ylabel("Value")
plt.title("Distribution of Survey Scores")
plt.show()
