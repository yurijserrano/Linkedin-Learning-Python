'''
Example file for variables
'''

# Declare a variable and initialize it
f = 0
print(f)

# Re-declaring the variable
f = "abc"
print(f)


# Variables of different types
print("This is a string " + str(123))


# Global vs local variables in functions
def some_function():
    global f
    f="def"
    print(f)

some_function()
print(f)

# del f
