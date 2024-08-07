#PROBLEM SET 1

text= input("camel: ")

for i in text:
    if i.isupper():
        text= text.replace(i, "_"+ i.lower())

print(text)


#PROBLEM SET 2
amountDue=50
payment=0
currency= [5,10,25]

while payment< 50:
    coin= int(input("Insert Coin: "))

    if coin in currency:
        payment=amountDue - coin

    if amountDue>0:
        print("Amount Due: ", payment)
    
    else:
        print("You owe: ", amountDue)


#VOWELS
vowels= ["a", "e", "i", "o", "u", ]

word=input("Enter a word: ")




