import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

student_data = {
    'Age': [18, 19, 20, 17, 21, 18, 19, 22, 20, 19],
    'Height': [165, 172, 168, 160, 175, 170, 162, 180, 167, 169],
    'Weight': [65, 70, 62, 58, 75, 68, 60, 80, 65, 72],
    'Math': [85, 92, 78, 90, 75, 88, 82, 70, 86, 80],
    'Science': [90, 85, 78, 92, 82, 88, 75, 70, 84, 76],
    'English': [82, 78, 90, 85, 75, 92, 88, 80, 79, 84]
}

df = pd.DataFrame(student_data)
print("Data Summary:")
print(df.describe())

print("\nStatistical Measures:")
mean_age = df['Age'].mean()
print(f"Mean Age: {mean_age:.2f}")

var_height = df['Height'].var()
print(f"Variance of Height: {var_height:.2f}")

cov_math_science = df['Math'].cov(df['Science'])
print(f"Covariance of Math and Science Scores: {cov_math_science:.2f}")

corr_weight_english = df['Weight'].corr(df['English'])
print(f"Correlation between Weight and English Scores: {corr_weight_english:.2f}")

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.boxplot(data=df, x='Age')
plt.title('Age Distribution')

plt.subplot(2, 2, 2)
sns.scatterplot(data=df, x='Height', y='Weight')
plt.title('Height vs Weight')

plt.subplot(2, 2, 3)
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')

plt.subplot(2, 2, 4)
sns.violinplot(data=df, x='Math', y='Science', split=True)
plt.title('Math and Science Scores Distribution')

plt.tight_layout()
plt.show()
