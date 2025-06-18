# Function to generate Fibonacci series up to n terms
def fibonacci(n):
    a, b = 0, 1
    count = 0
    series = []
    
    while count < n:
        series.append(a)
        a, b = b, a + b
        count += 1
    
    return series

# Input: number of terms
n = int(input("Enter the number of terms for Fibonacci series: "))

# Generate and print the series
fib_series = fibonacci(n)
print(f"Fibonacci series with {n} terms:")
print(fib_series)
