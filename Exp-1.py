# List of items, each item is a dictionary with price and quantity
items = [
    {"price": 10.50, "quantity": 2},
    {"price": 5.25, "quantity": 5},
    {"price": 20.00, "quantity": 1},
]

total_cost = 0.0  # Using float for currency values

for item in items:
    total_cost += item["price"] * item["quantity"]

print(f"Total cost: ${total_cost:.2f}")
