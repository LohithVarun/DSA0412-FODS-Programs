import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

gene_expression_data = {
    'Gene': ['Gene1', 'Gene2', 'Gene3', 'Gene4', 'Gene5', 'Gene6', 'Gene7', 'Gene8', 'Gene9', 'Gene10'],
    'Brain': np.random.exponential(scale=2, size=10),
    'Heart': np.random.normal(loc=5, scale=1.5, size=10),
    'Liver': np.random.lognormal(mean=1, sigma=0.5, size=10),
    'Kidney': np.random.gamma(shape=2, scale=2, size=10),
    'Lung': np.random.poisson(lam=3, size=10)
}

gene_expression_df = pd.DataFrame(gene_expression_data)

def asymmetry_measure(data):
    skewness = stats.skew(data)
    kurtosis = stats.kurtosis(data)
    left_tail = np.mean(data[data < np.median(data)])
    right_tail = np.mean(data[data > np.median(data)])
    asymmetry = (right_tail - left_tail) / (right_tail + left_tail)
    return skewness, kurtosis, asymmetry

print("Asymmetry Measure for Gene Expression Levels:")
for tissue in gene_expression_df.columns[1:]:
    tissue_data = gene_expression_df[tissue]
    skewness, kurtosis, asymmetry = asymmetry_measure(tissue_data)
    print(f"{tissue}: Skewness={skewness:.2f}, Kurtosis={kurtosis:.2f}, Asymmetry={asymmetry:.2f}")

print("\nImpact of Data Transformation:")
transformed_df = gene_expression_df.copy()
transformed_df['Brain'] = np.log(transformed_df['Brain'])
transformed_df['Heart'] = np.sqrt(transformed_df['Heart'])
transformed_df['Liver'] = np.log1p(transformed_df['Liver'])

sns.clustermap(transformed_df.iloc[:, 1:], cmap='coolwarm')
plt.title('Hierarchical Clustering of Transformed Gene Expression Data')
plt.show()
