import pandas as pd

property_data = {
    'property_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'location': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'New York', 'San Francisco', 'Miami', 'Chicago', 'Seattle', 'Los Angeles'],
    'bedrooms': [3, 4, 2, 5, 3, 4, 3, 5, 4, 3],
    'area_sq_ft': [1500, 2200, 1800, 3000, 1700, 2400, 1900, 2800, 2500, 2000],
    'listing_price': [750000, 1200000, 450000, 900000, 800000, 1500000, 650000, 700000, 950000, 1100000]
}

property_df = pd.DataFrame(property_data)

avg_price_by_location = property_df.groupby('location')['listing_price'].mean().reset_index()
print("Average listing price by location:")
print(avg_price_by_location)

properties_more_than_4_bedrooms = property_df[property_df['bedrooms'] > 4]
num_properties_more_than_4_bedrooms = len(properties_more_than_4_bedrooms)
print(f"\nNumber of properties with more than 4 bedrooms: {num_properties_more_than_4_bedrooms}")

largest_property = property_df.loc[property_df['area_sq_ft'].idxmax()]
print(f"\nProperty with the largest area:")
print(largest_property)
