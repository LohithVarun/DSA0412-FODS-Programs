import pandas as pd

sales_data = {
    'product_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G', 'Product H', 'Product I', 'Product J'],
    'quantity_sold': [150, 200, 120, 180, 90, 250, 170, 130, 110, 220],
    'revenue': [7500, 12000, 9600, 10800, 6300, 20000, 13600, 9100, 8800, 17600]
}

sales_df = pd.DataFrame(sales_data)

top_products = sales_df.nlargest(5, 'quantity_sold')
print("Top 5 products by quantity sold:")
print(top_products[['product_name', 'quantity_sold']])
