class Integer:
    def __init__(self, value):
        self.value = value

    def is_palindrome(self):
        # Convert the integer to a string
        string = str(self.value)

        # Reverse the string
        reversed_string = string[::-1]

        # Check if the original string and the reversed string are equal
        return string == reversed_string


# Example usage:

integer = Integer(1221)

# Check if the integer is a palindrome
is_palindrome = integer.is_palindrome()

# Print the result
print("Condition for Palindrome is ", is_palindrome)
