x= int(input("whats x? "))
y= int(input("Whats y? "))


if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")


if x<y:
    print("x is less than y")
elif x>y:
    print("x is greater than y")
else:
    print("x is equal to y")


#the elif logic in this scenario allows you to use >= because it bypasses the first questions
score= int(input("Score: "))

if  score>=90:
   print("Grade: A")
elif  score >=80:
    print("Grade: B")
elif  score >= 70:
    print("Grade: C")
elif score>= 60: 
    print("Grade: D")
else:
    print("Grade: F")

#parity portion

x=int(input("What is x? "))

if x %2 ==0:    
    print("even")
else:
    print("Odd")

def main():
    x= int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2==0 
    #part below is other, longer way to write this
    #if n % 2==0:
     #   return True
    #else:
     #   return False

main()


#HOUSE PORTION

name= input("whats ur name? ")

if name== "Harry" or name== "Hermione" or name== "Ron":
    print("Gryffindor")
elif name== "Draco":
    print("Slytherin")
else:
    print("Who? ")

name= input("whats ur name? ")

match name:
    case "Harry" | "hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")


def main():
    difficulty=input("Do you want difficult or casual? ")
    players=input("Multiplayer or single-player? ")

    if difficulty== "Difficult":
        if players== "Multiplayer":
            recommend("Poker")
        
        else:
            recommend("Klon")
    elif difficulty== "Casual":
        if players== "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")
    else:
        print("Enter a valid difficulty")



def recommend (game):
    print("You might like", game)

main()
