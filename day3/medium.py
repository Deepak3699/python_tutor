# 1 Program for Take age & ID yes/no → check if allowed to vote
# Ask the user to input their age
age = int(input("Enter your age: "))

# Ask if the user has an ID (yes/no)
has_id = input("Do you have an ID (yes/no)? ").strip().lower()

# Check voting eligibility: age must be 18 or older AND user must have an ID
if age >= 18 and has_id == "yes":
    print("You are allowed to vote")
else:
    print("You're not allowed to vote")


# 2 Take two strings → print True if both have length > 3
# Take two strings as input
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

# Check if both strings have length greater than 3
if len(s1) > 3 and len(s2) > 3:
    print("True")   # Both strings are longer than 3 characters
else:
    print("False")  # At least one string is 3 or fewer characters