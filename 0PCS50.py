#1ST QUESTION ON PROBLEM SET
#name=input("What is your name? ").lower()
#print(name)


#2ND QUESTION ON PROBLEM SET
#print("Create a three letter sentence")
#one= input("Enter the first word: ")
#two= input("Enter the second word: ")
#three= input("Enter the third word: ")

#print(one + "..." + two + "..." + three)

#3RD` EINSTEIN`
#c=3 * 10**8

#mass=int(input("enter mass amount: "))
#energy= mass * c**2

#print("the equation is equal to " , energy )

#4TH TIP CALCULATOR
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", ""))


def percent_to_float(p):
    return float(p.replace("%", ""))/100


main()
