#This is a number guessing game
import random
MAX_NUMBER = 10
MIN_NUMBER = 0
player_score = 0
Rounds = 0

def get_random_number():
    rn: int = random.randint(MIN_NUMBER, MAX_NUMBER)
    return rn

def play_game(rounds, score):
    computer_choice = get_random_number()
    name = input("Hey There! What's your name? ")
    print(f"Think you can guess the number I'm thinking of {name.title()}? Well, let's find out!")
    while True:
        choice = input("Type S to start the game or Q to quit: ")
        print("")
        if choice.isalpha():
            if choice.lower() == "s":
                guess = input(f"Please enter a random number from {MIN_NUMBER} to {MAX_NUMBER}: ")
                rounds += 1
                if guess.isdigit():
                    guess = int(guess)
                    if guess == computer_choice:
                        print("Correct! You guessed right!")
                        print("")
                        score += 1
                    elif guess > MAX_NUMBER:
                        print(f"Cannot enter a number greater than {MAX_NUMBER}")
                    else:
                        print("Aww! That wasn't my choice.")
                else:
                    print("Please enter a valid number.")
            elif choice.lower() == "q":
                print(f"Rounds Played: {rounds}")
                print(f"Your score: {score}")
                print(f"Good game! Until we meet again {name.title()}.")
                exit()
            else:
                print("Please select an option.")
        else:
                print("Please select an answer.")


play_game(Rounds, player_score)






