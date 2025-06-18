# Initial values
a = 5
b = 10

print(f"Original values: a = {a}, b = {b}")

# Swap using a temporary variable
temp = a
a = b
b = temp

print(f"After swap with temporary variable: a = {a}, b = {b}")

# Swap back without using a temporary variable
a, b = b, a

print(f"After swap without temporary variable: a = {a}, b = {b}")
