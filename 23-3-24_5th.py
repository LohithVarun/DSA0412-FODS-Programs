
customer_demographics = {
  "customer_id": [1, 2, 3, 4, 5],
  "age": [25, 32, 40, 18, 55],
  "gender": ["Male", "Female", "Male", "Female", "Male"],
  "location": ["New York", "California", "Texas", "Florida", "Chicago"]
}

user_activity_logs = {
  "customer_id": [1, 1, 2, 3, 4, 5],
  "timestamp": ["2024-03-24 10:00", "2024-03-24 15:00", "2024-03-23 12:00", "2024-03-22 08:00", "2024-03-21 17:00", "2024-03-20 11:00"],
  "page_views": [5, 10, 3, 7, 2, 8],
  "interaction_duration": [60, 120, 45, 90, 30, 100]
}

customer_support = {

  "customer_id": [2, 3, 4, 5],
  "support_tickets": [1, 2, 0, 3],
  "satisfaction_score": [7, 5, 9, 8]
}
import pandas as pd
customer_demographics_df = pd.DataFrame(customer_demographics)
user_activity_logs_df = pd.DataFrame(user_activity_logs)
customer_support_df = pd.DataFrame(customer_support)

merged_data = customer_demographics_df.merge(user_activity_logs_df, on="customer_id")
merged_data = merged_data.merge(customer_support_df, on="customer_id")

print(merged_data.head())

merged_data.to_csv("consolidated_customer_data.csv", index=False)
