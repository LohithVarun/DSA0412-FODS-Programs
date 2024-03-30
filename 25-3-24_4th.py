item_prices = [4.99, 2.75, 6.25, 1.89, 3.49]
item_quantities = [2, 1, 3, 4, 1]

discount_rate = 0.15
tax_rate = 0.08

subtotal_before_discount = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))
discount_amount = subtotal_before_discount * discount_rate
subtotal_after_discount = subtotal_before_discount - discount_amount
tax_amount = subtotal_after_discount * tax_rate
total_cost = subtotal_after_discount + tax_amount

print(f"Subtotal before discount: ${subtotal_before_discount:.2f}")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Subtotal after discount: ${subtotal_after_discount:.2f}")
print(f"Tax amount: ${tax_amount:.2f}")
print(f"Total cost: ${total_cost:.2f}")
