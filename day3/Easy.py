# 1 Add two numbers & print the result

def total(a, b): # create a function using def 
    result = a + b # add two numbers 
    return result # return the result

first_num =int(input("enter the first number "))
second_num = int(input("enter the second number "))

print(total(first_num, second_num)) # calling the function 
# OUTPUT sum of two numbers 

# 2 Take two numbers and print the remainder

def rem(a,b): # Function
    if b == 0:
        return "Error: division by zero"
    result = a % b 
    return result

a = int(input("enter the first number "))
b = int(input("enter the second number "))

print(rem(a,b))

# 3 Check if a number is greater than 50
num = int(input("Enter an integer number: "))

# Check if the number is greater than 50
if num > 50:
    # If condition is true, print this message
    print(f"Number {num} is greater than 50")
else:
    # Otherwise, print this message
    print(f"Number {num} is smaller than or equal to 50")

