# Simulate utilities.math_utils module
class math_utils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

# Simulate utilities.string_utils module
class string_utils:
    @staticmethod
    def to_uppercase(s):
        return s.upper()

    @staticmethod
    def to_lowercase(s):
        return s.lower()


# Program using the "package"
def main():
    print("Addition of 5 and 3:", math_utils.add(5, 3))
    print("Subtraction of 5 and 3:", math_utils.subtract(5, 3))
    print("Uppercase of 'hello':", string_utils.to_uppercase('hello'))
    print("Lowercase of 'WORLD':", string_utils.to_lowercase('WORLD'))

if __name__ == "__main__":
    main()
