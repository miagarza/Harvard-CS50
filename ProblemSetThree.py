"""
Syntax errors: on YOU to solve, typo



run time errors:
happen as your code is running, you then have to write code "defensively"
to detect when they show up. based off bad user input 

Value Error: input error, so you should program defensivley 


"""

#try & except
"""
try:
    x= int(input("Whats x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
"""


#what if input isnt an int????
#test corner cases!!!


#value error happening too soon

"""
try:
    x=int(input("Whats x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
"""


"""
while True:
    try:
        x=int(input("Whats x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")
"""

"""
#return can break you out of a loop and will return a value for you
def main():
    x= get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x=int(input("Whats x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()
"""


#return can break you out of a loop and will return a value for you
#only pass when there is an exception of a value error


def main():
    x= get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()


#breakpoints- allows you to specify on what lines of codes do you
#want to pause or break so you can look more into the code
#you would hover to the left of the line number and then vs would
#stop it running at that specific point


#raise is when you call an error if the input
#doesnt match up with the input/methods function