import random
userno = int(input("Guess a number b/w 1 to 5:"))
number=random.randint(1,5)
if userno == number:
    print("Your guess is right")
else:
    print("You loss. \nComputer number was:",number)
