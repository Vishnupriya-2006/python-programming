# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Count occurrences of a character in a string
def count_char(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count

# 3. Replace characters in a string
def replace_char(s, old, new):
    result = ""
    for c in s:
        if c == old:
            result += new
        else:
            result += c
    return result

# Example usage:
text = "hello world"
print(f"Original string: {text}")

# Reverse
print(f"Reversed string: {reverse_string(text)}")

# Count character 'l'
char_to_count = 'l'
print(f"Count of '{char_to_count}': {count_char(text, char_to_count)}")

# Replace 'o' with '0'
print(f"String after replacing 'o' with '0': {replace_char(text, 'o', '0')}")
