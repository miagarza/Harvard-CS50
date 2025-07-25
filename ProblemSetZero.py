"""
name=input("Whats your name? ")
name.split(" ")
print(name)
"""

############################################

"""
print("hello,", name)
#print(name)

print("Hello, 'friend'")
"""
#######################

"""
name=input("What is your name? ").strip().title()



#removes white space from string
name=name.strip()

#capitalizes the whole thing
name=name.upper()

#capitalizes only the first letter 
name=name.capitalize()

print("hello,", name)
"""

########################
"""
name=input("Whats your name? ").strip().title()
name.split(" ")

print(f"hello, {name}")

"""
##########################

"""
x=int(input("What's x? "))
y=int(input("What's y? "))

print(x+y)
"""
###########################

""""
x=float(input("What's x? "))
y=float(input("What's y? "))

z=x/y
#:.2f means to round the result to 2 decimal places
print(f"{z:.2f}")
#z=round(x+y)
#print(f"{z:,}")

"""

#########################
"""
def hello(to="world"):
    print("Hello,", to)

hello()
name=input("What's your name? ")
hello(name)
"""
################

"""
def main():
    hello()
    name=input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello", to)


main()
hello()
"""

#########################

"""
def main():
    x=int(input("What is x squared? "))
    print("x squared is", squared(x))

#using return here allows you to pass the value to another spot
def squared(n);
    return n*n
"""

#####################
"""
#problem set 0, 1

greeting=input("Say:").title().lower()
print(greeting)
"""

#########################
"""
#problem set 0,2
intro=input("")
intro=intro.replace(" ","...")
print(intro)
"""
#######################

"""
#problem set 0,3
prompt=input("")

if ":)" in prompt:
    print("hello happy face")
if ":(" in prompt:
    print("goodbye sad face")
"""
########################
"""
#problem set 0,4

c=int(300000000)
c=c*c

m=int(input("m= "))
e=m*c
print(int(e))
"""
#########################
"""
#problem set 0,5

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d=d.replace("$", " ")
    return float(d)


def percent_to_float(p):
    p=p.replace("%"," ")
    return float(p)/100


main()

"""