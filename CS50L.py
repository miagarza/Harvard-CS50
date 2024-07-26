#asking user for name
name= input("Whats ur name? ")
print("hello, " , name, sep="???")
print(name)

name= input("what is ur name? ").strip().title()
#below gets rid of extra white space and capa user name
name= name.strip().title()
name= name.title()

#split users name into first and last
first , last =name.split(" ")

print(f"hello, {first}")  
#f allows the format to be different instead of just doing pluses

x=float(input("What's x? "))
y=float(input("what's y? "))

z= round (x/y, 2)

print(f"{z:.2f}")
print(f"{z:,}")

#NEWNEWNEWNEW
#python is going to treat every line of code under given as the meaning of the func hello
#the name of the parameter is "to"
def hello(to="world"):
    print("hello,", to)

#the function is taking the value of the parameter as input
hello()
name= input("What's ur name? ")
hello(name)


#extra
def main():
    name=input("Whats ur name? ")
    hello(name)


def hello (to="world")
    print("hello,", to)

main()

def main():
    print("Hello world!")
    print("This is CS50P.")

main()
def is short for define

def get_guess():
    guess= int(input("Enter a guess: "))
    return guess

def main():
    guess= get_guess()
    if guess == 50:
        print("Correct")
    else:
        #print("Incorrect!")
    print(guess)

main()

print(get_guess())

emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    emoticon= ":D"
    say("Oh, hi!")

def say(phrase):
    print(phrase + " "+ emoticon)

main()