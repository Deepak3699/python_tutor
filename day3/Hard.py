""" Write a program to check:

A student passes if:
- marks >= 33
- and attendance >= 75 """

marks = int(input(" Enter students marks "))
attendance = int(input(" Enter students attendance "))

if marks >= 33 and attendance >= 75:
    print(" Student Pass")
else:
    print(" Student fail ")