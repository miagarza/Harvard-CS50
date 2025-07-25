#lecture and problem set #1

"""
x=int(input("What's x? "))
y=int(input("What's y? "))

if x<y:
    print("x is less than y")

elif x>y:
    print("x is greater than y")

else:
    print("x is equal to y")
"""

"""
x=int(input("What's x? "))
y=int(input("What's y? "))

if x!=y:
    print("x is not equal to y")
else:
    print("x is equal to y")
"""


"""
#showing mulitple ways to type the question
score=int(input("score: "))

if score>=90:
    print("Grade: A")
elif score>=80:
    print("Grade: B")


elif 70<= score <= 80:
    print("Grade: C")
elif 60<= score <= 70:
    print("Grade: D")
else:
    print("Grade: F")
"""

"""
x= int(input("what's x? "))

if x% 2==0:
    print("Even")
else:
    print("Odd")
"""

"""
def main():
    x=int(input("What's x? "))
    if is_even(x):
        print()
    else:
        print("Odd")



#def is_even(n):
    #if n%==0:
        #return True
    #else:
        #return False

        

#"pythonic" way to write this ^ down below
#since you are already checking if its true, and the 
#function knows its either going to be true or false
#you can make it shorter

def is_even(n):
    #return True if n%2==0 else False
    return n%2==0

main()
"""

"""
name=input("Whats ur name? ")


#if name== "harry" or name== "ron" or name=="hermione"
    #print("gryf")
#elif name=="draco":
    #print("slyrn")
#else:
    #print("who?")

match name:
    case"Harry" | "hermione" | "Ron":
        print("gryf")
    case "draco":
        print("sly")
    case _:
        print("Who?")
#^^^ case _: means what ever hasnt been handled (else)

"""

"""
#absolutley random thing i didnt realize until now
def ok():
    x=input("what do you want? ")
    if x=="ice cream":
        recc("Choco")
    else:
        recc("burger")

def recc(x):
    print("you might like", x)

ok()
"""

"""
#deep thought

def test():
    a=input("What is the Answer to the great question of life, the universe, and everything? ")
    a=a.lower()
    match a:
        case"forty two" | "forty-two" | "42":
            print("Yes")
        case _: 
            print("No")

test()
"""

"""
#HFSB


def money():
    greeting=input("Greeting: ")
    if "hello" in greeting:
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")


money()
"""


"""
#file extensions
def ext():
    file_name=input("File Name:")
    if file_name.endswith(".gif"):
        print("image/gif")
    if file_name.endswith(".jpeg") or file_name.endswith(".jpg"):
        print("image/jpeg")
    if file_name.endswith(".png"):
        print("image/png")
    if file_name.endswith(".pdf"):
        print("image/pdf")
    if file_name.endswith(".txt"):
        print("image/txt")
    if file_name.endswith(".zip"):
        print("image/zip")
    else:
        print("application/octet-stream ")


ext()
"""

"""
#math

def interp():
    express=input("Expression: ").split()
    x=float(express[0])
    y=express[1]
    z=float(express[2])
    mathy(x,y,z)


def mathy(x,y,z):
    if y=="+":
        final= x + z
    if y=="-":
        final= x - z 
    if y=="*":
        final= x*z
    if y=="/":
        final= x/z
    print(final)
    

interp()
"""


#meal time

"""   
def mathy(time):
    time=time.split(":")
    print(time)
    whole= float(time[0])
    deci=float(time[1])
    num=float(deci/60)
    final=(whole + num)
    return final 
"""


def mathy(time):
    time=time.split(":")
    print(time)
    whole= float(time[0])
    deci=float(time[1])
    num=float(deci/60)
    done=(whole , num)


def meal():
    if 7.0<= done <= 8.0:
        print("breakfast time")
    if 12.0<= done <= 13.0:
        print("lunch time")
    if 18.0<= done <= 19.0:
        print("dinner time")
    
    



time=input("What time is it? ")
meal()