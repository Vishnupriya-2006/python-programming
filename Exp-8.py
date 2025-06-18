# 1. Number series: Even numbers up to n
def even_numbers(n):
    print(f"Even numbers up to {n}:")
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, end=' ')
    print('\n')

# 2. Number pattern: Incremental numbers in rows
def number_pattern(rows):
    print(f"Number pattern with {rows} rows:")
    for i in range(1, rows+1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()  # new line after each row
    print()

# 3. Pyramid pattern using stars (*)
def pyramid_pattern(rows):
    print(f"Pyramid pattern with {rows} rows:")
    for i in range(1, rows+1):
        # Print spaces
        for _ in range(rows - i):
            print(' ', end='')
        # Print stars
        for _ in range(2*i - 1):
            print('*', end='')
        print()  # new line after each row
    print()

# Example usage:
n = 10
even_numbers(n)

rows = 5
number_pattern(rows)

pyramid_pattern(rows)
