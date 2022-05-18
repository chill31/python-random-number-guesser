#importing required modules.

import math
import random

# generating a random user ID.
randomUserID = math.floor(random.randint(11111111, 9999999999))

# giving an introduction to the game.
print(f"""
Hello, welcome to the random number guessing game! First, before playing the game, please enter some information:
""")

modes = [
 "1-10",
 "1-50",
 "1-100"
]

# selected number range (default: easy)
selected = [1, 10]

# taking their name.
name = input("Please enter a name:\n> ").split(" ")


# taking the mode input.
enteredMode = input(f"""
Hi {name[0]}! Your session ID this time is: {randomUserID}.
Please enter a game-mode to play on:

- Easy: 1-10
- Medium: 1-50
- Hard: 1-100

you can also type in hint when it asks for the guess, it shows a hint.


Please enter either easy, medium or hard in the input given below:
> """)


# default guesses and hints.
guesses = 5
hints = 5


# checking for the selected mode.

if enteredMode.lower() == "easy":
    print("You chose easy mode!")
    selected = [1, 10]
    guesses = 3
    hints = 1
elif enteredMode.lower() == "medium":
    print("You chose medium mode!")
    guesses = 6
    hints = 3
    selected = [1, 50]
elif enteredMode.lower() == "hard":
    print("You chose hard mode!")
    selected = [1, 100]
    guesses = 8
    hints = 4
else:
    print("That's not a valid option! Setting game-mode to \"Easy\"")


# generating the random number for the game.
randomNumber = str(math.floor(random.randint(selected[0], selected[1])))


# while the game is on, we keep asking the user for guesses.
while True:
    guess = input("\nenter your guess\n> ")

    if guesses == 0:
        print(f"You lost! The random number was {randomNumber}")
        #breaking the while loop if no guesses are left.
        break

    if guess == "hint":
        if hints == 0:
            print(f"You used up all of your {hints} hints")
        else:
            hints -= 1
            if selected == [1, 10]:

                num = 5

                if int(randomNumber) > num:
                    print(f"The Random Number is bigger than {num}")
                elif int(randomNumber) < num:
                    print(f"The Random Number is smaller than {num}")
                elif int(randomNumber) == num:
                    print(f"Hints are not available for this game!")


            elif selected == [1, 50]:
                num = 25

                if int(randomNumber) > num:
                    print(f"The Random Number is bigger than {num}")
                elif int(randomNumber) < num:
                    print(f"The Random Number is smaller than {num}")
                elif int(randomNumber) == num:
                    print(f"Hints are not available for this game!")

            elif selected == [1, 100]:
                num = 50

                if int(randomNumber) > num:
                    print(f"The Random Number is bigger than {num}")
                elif int(randomNumber) < num:
                    print(f"The Random Number is smaller than {num}")
                elif int(randomNumber) == num:
                    print(f"Hints are not available for this game!")
    elif guess.lower() == "quit":
        confirm = input("Are you sure you want to quit? (y/n)\n> ")
        if confirm.lower() == "y" or confirm.lower() == "yes":
            print("You forefit the game.")
            quit()
        else:
            print("Close Call buddy! Come on now, continue with the game: ")
            continue

    else:
        guesses -= 1
        if guess != randomNumber:
            print(f"That was not correct! Guess again. You have {guesses + 1} guesses and {hints} hints left")
        elif guess == randomNumber:
            print(f"You won! You had {guesses + 1} guesses and {hints} hints left to use.")
            playAgainMsg = input("Do you want to play again? (y/n)\n> ")
            if playAgainMsg.lower() == "y" or playAgainMsg.lower() == "yes":
                print("You chose to play again, Please enter some information again: ")
                print("Unfortunately, we cannot do this with code, you will have to terminate the process and start it again.")
            else:
                print("You left the game.")
                quit()

#end
