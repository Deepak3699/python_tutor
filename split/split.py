# Split Break a string into parts
''' Imagine you have a sentence and want to cut it into words wherever there is a space.
📌 Why we need it:
To process sentences
To read user input
To analyze text (very common in real apps)'''

text = " I love python "
words = text.split()  # Default separator = space , Output is a list
print(words)

# Using custom separator 

data = " apple,git  mango, banana"
fruits = data.split(",")
print(fruits)

