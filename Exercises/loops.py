'''
Example file for working with loops
'''

def main():
    x = 0

    # define a while loop
    while (x < 5):
        print(x)
        x = x + 1

    # define a for loop
    for x in range(5,10):
        print(x)

    # use a for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]
    for d in days:
        print(d)

    # use the break statement
    for x in range(5,10):
        if(x == 7): break
        print(x)

    # use the continue statement
    for x in range(5,10):
        if(x % 2 == 0): continue
        print(x)

    # using the enumerate()
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):
        print(i, d)


if __name__ == '__main__':
    main()