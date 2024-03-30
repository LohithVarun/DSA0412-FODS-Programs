import pandas as pd
import matplotlib.pyplot as plt

scores = [85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 5, 98, 72]

data = {'scores': scores}
df = pd.DataFrame(data)

print("descriptive statistics:")
print(df['scores'].describe())

q1 = df['scores'].quantile(0.25)
q3 = df['scores'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)
potential_outliers = df[~df['scores'].between(lower_bound, upper_bound)]

if not potential_outliers.empty:
  print("\nPotential outliers:")
  print(potential_outliers)

plt.boxplot(df['scores'])
plt.xlabel('Scores')
plt.ylabel('Value')
plt.title('Box Plot of Scores Distribution')
plt.show()
