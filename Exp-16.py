def int_to_roman(num):
    # Define tuples of Roman numerals and their corresponding values
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_num = ""
    i = 0
    while num > 0:
        # Find how many times the current value fits into num
        count = num // val[i]
        # Append the corresponding symbol count times
        roman_num += syms[i] * count
        # Decrease num by the amount converted
        num -= val[i] * count
        i += 1
    return roman_num

# Get input from the user
number = int(input("Enter an integer to convert to Roman numeral: "))

# Basic validation for positive integers
if number <= 0:
    print("Please enter a positive integer greater than zero.")
else:
    print(f"Roman numeral: {int_to_roman(number)}")
