import numpy as np

house_data = {
    'bedrooms': [3, 4, 2, 5, 3, 4, 6, 3, 4, 5],
    'square_feet': [1500, 2200, 1200, 3000, 1800, 2400, 3500, 1700, 2100, 2800],
    'sale_price': [300000, 450000, 220000, 600000, 350000, 480000, 750000, 320000, 400000, 580000]
}

house_array = np.array(list(house_data.values())).T
more_than_4_bedrooms = house_array[house_array[:, 0] > 4]
avg_sale_price = np.mean(more_than_4_bedrooms[:, 2])

print(f"The average sale price of houses with more than 4 bedrooms is: ${int(avg_sale_price):,}")
