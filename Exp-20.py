def frequency_of_values(d):
    freq = {}
    for value in d.values():
        freq[value] = freq.get(value, 0) + 1
    return freq

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

freq = frequency_of_values(sample_dict)
print("Frequency of all values:", freq)
