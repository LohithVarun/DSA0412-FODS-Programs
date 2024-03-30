import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew

np.random.seed(42)
exam_scores = np.random.normal(loc=75, scale=10, size=50)
exam_scores = np.round(exam_scores)
exam_scores = np.clip(exam_scores, 40, 100) 
mean_score = np.mean(exam_scores)
median_score = np.median(exam_scores)
skewness = skew(exam_scores)

plt.figure(figsize=(8, 6))
plt.hist(exam_scores, bins=15, edgecolor='black')
plt.axvline(mean_score, color='r', linestyle='--', label='Mean')
plt.axvline(median_score, color='g', linestyle='--', label='Median')
plt.xlabel('Exam Score')
plt.ylabel('Frequency')
plt.title('Distribution of Exam Scores')
plt.legend()
plt.show()
if abs(skewness) < 0.5:
    print("The distribution of exam scores is approximately symmetric.")
else:
    print("The distribution of exam scores is skewed.")

print(f"Mean score: {mean_score:.2f}")
print(f"Median score: {median_score:.2f}")
print(f"Skewness: {skewness:.2f}")
