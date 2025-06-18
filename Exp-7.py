import math

# 1. Factorial function
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 2. Largest number in a list
def largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# 3. Area of different shapes
def area_of_shape(shape, **kwargs):
    shape = shape.lower()
    if shape == "circle":
        radius = kwargs.get("radius", 0)
        return math.pi * radius * radius
    elif shape == "rectangle":
        length = kwargs.get("length", 0)
        width = kwargs.get("width", 0)
        return length * width
    elif shape == "triangle":
        base = kwargs.get("base", 0)
        height = kwargs.get("height", 0)
        return 0.5 * base * height
    else:
        return "Shape not supported"

# Testing the functions:

# Factorial
num = 5
print(f"Factorial of {num} is {factorial(num)}")

# Largest number
lst = [3, 7, 2, 9, 5]
print(f"Largest number in {lst} is {largest_number(lst)}")

# Area of shapes
print(f"Area of circle with radius 4: {area_of_shape('circle', radius=4):.2f}")
print(f"Area of rectangle 5x3: {area_of_shape('rectangle', length=5, width=3)}")
print(f"Area of triangle with base 6 and height 4: {area_of_shape('triangle', base=6, height=4)}")
