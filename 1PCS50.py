#CASES CHALLENGE
ques=input("What is the answer to the Great Question of Life and stuff? ")

if ques== "42" or ques== "forty two" or ques== "forty-two":
    print("Yes")

#BANK TELLER CHALLENGE
greeting=input("What do you say? ")
specChara="h"

if greeting=="hello":
    print("Here is $0")
elif specChara in greeting:
    print("Here is $20")
else:
    print("Here is $100")

#FILE TYPE CHALLENGE
fileType= input("Enter file name: ")
start_index=5
end_index=9

substring=fileType[start_index:end_index]
print("image/"+ substring)

#MATH INTERPRETER


# Get input from the user
eq = input("Enter an equation: ")

# Split the input into components
x_str, y, z_str = eq.split()

# Convert x and z to floats
x = float(x_str)
z = float(z_str)

# Perform the operation based on the operator
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z

# Print the result formatted to one decimal place
print(f"{result:.1f}")

x=float
z=float


