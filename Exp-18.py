def find_max_min(tup):
    max_element = max(tup)
    min_element = min(tup)
    return max_element, min_element

# Example usage:
input_tuple = (12, 45, 7, 34, 89, 2, 5)

max_val, min_val = find_max_min(input_tuple)
print(f"Maximum element: {max_val}")
print(f"Minimum element: {min_val}")
