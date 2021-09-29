#Author: JD 09/29/2021

card_1 = int(input("Please enter the first number: "))

card_2 = int(input("Please enter the second number: "))

if card_1 + card_2 >= 21:
    print("You are busted.")
else:
    print("You are safe.")