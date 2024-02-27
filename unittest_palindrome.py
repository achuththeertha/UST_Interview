def is_palindrome(string):
    """Checks if a string is a palindrome.

    Args:
        string: The string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """

    reversed_string = string[::-1]
    return string == reversed_string

# Positive unit tests
assert is_palindrome("racecar")
assert is_palindrome("madam")
assert is_palindrome("121")

# Negative unit tests
assert not is_palindrome("hello")
assert not is_palindrome("world")
assert not is_palindrome("123")
