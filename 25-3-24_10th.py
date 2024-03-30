import matplotlib.pyplot as plt
import numpy as np

sales_data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'sales': [25000, 28000, 31000, 26000, 29000, 32000, 35000, 30000, 27000, 33000, 28000, 36000]
}

months = sales_data['month']
sales_values = sales_data['sales']

plt.figure(figsize=(10, 6))
plt.plot(months, sales_values, marker='o')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Data (Line Plot)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(np.arange(len(months)), sales_values)
plt.xlabel('Month Index')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Data (Scatter Plot)')
plt.xticks(np.arange(len(months)), months, rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(months, sales_values)
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Data (Bar Plot)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
