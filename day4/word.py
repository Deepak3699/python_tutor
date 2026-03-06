text = "Python"
print(text[0], text[-1])   # first and last 

tx = "  pythonna  "
print(tx.upper())   # → "  PYTHONNA  "
print(len(tx))      # → 11 (because of spaces)

#Medium

# Reverse the string
print(tx[::-1])     # → "  annhtyp  "

# Count how many times 'a' appears
print(tx.count("a"))  # → 2

# Remove spaces from beginning & end
print(tx.strip())   # → "pythonna"

#hard
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Examples
print(is_palindrome("madam"))       # True
print(is_palindrome("Python"))      # False
print(is_palindrome("racecar"))     # True
print(is_palindrome("Never odd or even"))  # True


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Take user input
user_input = input("Enter a word or phrase: ")

# Call the function and print the result (True/False)
print(is_palindrome(user_input))