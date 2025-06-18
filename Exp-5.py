import math

# 1. Exchange the values of two variables
a = 5
b = 10
print(f"Before exchange: a = {a}, b = {b}")

# Exchange values
temp = a
a = b
b = temp

print(f"After exchange: a = {a}, b = {b}\n")

# 2. Circulate (rotate) the values of n variables to the right by one position
values = [1, 2, 3, 4, 5]
print(f"Original list: {values}")

# Rotate right by one
last = values[-1]
for i in range(len(values)-1, 0, -1):
    values[i] = values[i-1]
values[0] = last

print(f"List after circulation: {values}\n")

# 3. Calculate distance between two points (x1, y1) and (x2, y2)
x1, y1 = 2, 3
x2, y2 = 7, 8

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance between points ({x1},{y1}) and ({x2},{y2}) is {distance}")
