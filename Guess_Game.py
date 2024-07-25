#Guess_Game
from random import randint

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
print("WELCOME TO THE GUESS GAME")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>")

SIZE = 10
count = 0
for i in range(SIZE):
    number = randint(0, 10)
    print("--------------------------------------------------")
    guess = int(input("==> Enter a number between (1 to 10): "))
    print("--------------------------------------------------")
    if number == guess:
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("==>YOU WON!<==, The number was ", guess, "!!!!")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        count += 1
        break
    elif guess > number:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Sorry... This time the number was ", number)
        print("Your guess was larger :(")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    elif guess < number:
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("Sorry... This time the number was ", number)
        print("Your guess was Smaller :(")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

if count == 0:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("===> G-A-M-E O-V-E-R <===")
    print("! ! YOU RAN OUT OF CHANCES ! !")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
