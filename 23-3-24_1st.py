import pandas as pd
weathers = ['Sunny', 'Cloudy', 'Sunny', 'Cloudy', 'Rainy', 'Cloudy', 'Cloudy', 'Rainy', 'Cloudy', 'Cloudy', 'Sunny', 'Cloudy', 'Sunny', 'Cloudy', 'Cloudy', 'Sunny', 'Cloudy', 'Rainy']

df = pd.DataFrame({"weathers":weathers})
fr = df.groupby(by="weathers").size()
print("Frequencies:\n",fr)
print("\nMost highest occuring Weather:",fr.idxmax())
