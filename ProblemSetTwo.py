#Loops,Videos 3


"""
#meow meow meow

i=1

while i < 3:
    print("meow")
    i=i+1

"""


"""
#using _ can be a placeholder for i and it shows its just a 
#variable that ur not using later 


for _ in range(3):
    print("Meow")

print("meow\n" *3, end="")

"""

"""
while True:
    n=int(input("What's n? "))
    if n>0:
        break
   

for _ in range(n):
    print("meow")
"""

    
"""
def main():
    number= get_number()
    meow(number)


def get_number():
    while True:
        n=int(input("What's n? " ))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("Meow")

main()

"""


"""
students= ["Harry", "Ron", "Hermione"]


#for students in students:
#    print(students)

for i in range(len(students)):
    print(i+1 , students[i])
"""



"""
students={"herm": "gryf", 
          "Harry": "Gryff",
          "draco": "slyrn"
}


#print(students["herm"])
#print(students["draco"])

for student in students:
    print(student, students[student], sep=", ")


# in line 84, students[student] is different than the student right 
#before it because the second variable is getting the value
# (which is gryff) using the key (harry)
"""

"""
#another hp dict
#lists have square brackets 
#dict have curly brackets 


students=[
    {"name": "Herm", "house": "gryf", "patr": "otter"},
    {"name": "harry", "house": "gryf", "patr": "stag"},
    {"name": "ron", "house": "gryf", "patr": "jack"},
    {"name": "draco", "house": "slyrn", "patr": None},
]

for students in students:
    print(students["name"], students["house"], students["patr"], sep=", ")
"""


"""
def main():
    print_column(3)


def print_column(height):
    for _ in range(height):
        print("#")

main()
"""
"""
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()


"""

"""
def main():
    print_square(3)


def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            # print brick 
            print("#", end="")
        print()

main()
"""


"""
def main():
    print_square(3)


def print_square(size):
    #for each row in square
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#"* width)


main()
"""

#################################################################
#problem sets!


"""
#1- camelCase


def camelcase():
    name=input("camelCase: ")
    

    print(name)



"""


#2- Coke

"""
ad=50

while ad != 0:
    print("Amount Due:", ad)
    payment=int(input("Insert Coin: "))
    ad=ad-payment 
print("Change Owed:", ad)
"""


"""
#3- twttr

def no_vwls():
    here= input("Input: ")
    here=here.lower().replace("a","")
    print("Output:"+ here)

no_vwls()
"""


#3- vanity plates



#4- Nurtition Facts

foods={
    "name": "apple", "calories": 130,
    "name": "avocado", "calories": 50,
    "name": "banana", "calories": 110,
    "name": "cantaloupe", "calories": 50,
    "name": "grapes", "calories": 90,
    "name": "honeydew", "calories": 50,
    "name": "lemon", "calories": 15,
    "name": "strawberries", "calories": 50,
    "name": "watermelon", "calories": 80,
}

def food():
    item=input("Item: ")
    print(f"Calories: {foods["calories"]}" )

food()