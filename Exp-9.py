# Function to find GCD using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find LCM using GCD
def lcm(a, b):
    return (a * b) // gcd(a, b)

# Input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate GCD and LCM
gcd_value = gcd(num1, num2)
lcm_value = lcm(num1, num2)

print(f"GCD of {num1} and {num2} is: {gcd_value}")
print(f"LCM of {num1} and {num2} is: {lcm_value}")
