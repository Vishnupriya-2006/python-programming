def remove_even_numbers(numbers):
    # Use list comprehension to keep only odd numbers
    return [num for num in numbers if num % 2 != 0]

# Example usage:
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = remove_even_numbers(input_list)
print("List after removing even numbers:", result)
