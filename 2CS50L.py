

i=0
while i < 3:
    print("bark")
    i+=1


#same thing as above, this way is shorter
#instead of using i bc its kinda useless you cna just put _


for i in range(123):
    print("bark")

# other way to do is- 
#print("bark\n"*3, end="") 


#Lines 1-4 cause an infinite loop and checkign the number value
#the break statment breaks out of the while loop


while True:
    n= int(input("Whats n? "))
    if n > 0:
        break

for _ in range(n):
    print("Bark")




def main():
    number= get_number()
    bark(number)

def get_number():
    while True:
        n = int(input("Whats n? "))
        if n >0:
            break
    return n 

def bark(n):
    for _ in range(n):
        print("bark")

main()



students= ["Hermione", "Harry", "Ron"]

for i in range (len(students)):
    print(i, students[i])





students= ["Hermione", "Harry", "Ron", "Draco"]
houses= ["Gryf", "Gryff", "Gryff", "Slytherin"]


#values correpsond with houses and students in list
#you want to associate harry w grff and so on

#below is a dict


students= {"Hermione": "Gryff", 
           "Harry": "Gryff", 
           "Ron": "Gryff",
           "Draco": "Slyerthin"
}

for student in students:
    print(student, students[student], sep=" ,")




students= [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" ,")




def main():
    print_row(4)


def print_row(width):
    print("?"* width)

main()


    

#this part means horizontal output
    
for _ in range(3):    
    print_column(3)

def print_column(height):
    print("#\n * height, end=")

main()


#making mario set up with has marks


def main():
    print_square(3)


def print_square(size):
    #for eahc row in square
    for i in range(size):
        for j in range(size):
            #for each brick in row
            print("#", end="")
            print()

main()



results=["Mario", "Luigi", "yo", "KT", "Toad", "Bowser", "DK jr."]


results.remove("Bowser")
results.insert(0, "Bowser")
results.reverse()
#results.append("Princess")
#results.append("Yoshi")
#results.append("Koopa Troopa")
#results.append("Toad")
#results.extend(["Bowser", "DK jr"])

print(results)


