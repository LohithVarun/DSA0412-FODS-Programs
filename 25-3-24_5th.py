import pandas as pd

order_data = {
    'customer_id': [1, 2, 3, 1, 2, 4, 2, 3, 1, 4],
    'order_date': pd.date_range(start='2023-01-01', end='2023-01-10', freq='D'),
    'product_name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product D', 'Product B', 'Product D', 'Product C', 'Product A', 'Product B'],
    'order_quantity': [2, 1, 3, 4, 2, 1, 3, 2, 1, 4]
}

order_df = pd.DataFrame(order_data)

orders_per_customer = order_df.groupby('customer_id')['product_name'].count().reset_index()
print("Total orders per customer:")
print(orders_per_customer)

avg_order_quantity = order_df.groupby('product_name')['order_quantity'].mean().reset_index()
print("\nAverage order quantity per product:")
print(avg_order_quantity)

earliest_order_date = order_df['order_date'].min()
latest_order_date = order_df['order_date'].max()
print(f"\nEarliest order date: {earliest_order_date}")
print(f"Latest order date: {latest_order_date}")
