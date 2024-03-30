import matplotlib.pyplot as plt

sales_data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'sales': [45000, 38000, 51000, 42000, 48000, 55000, 60000, 52000, 49000, 57000, 44000, 62000]
}

months = sales_data['month']
sales_values = sales_data['sales']

plt.figure(figsize=(10, 6))
plt.plot(months, sales_values, marker='o')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Data')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.bar(months, sales_values)
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.title('Monthly Sales Data')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
