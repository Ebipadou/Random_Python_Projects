import random

# Dictionary containing words and hints
words = {
    "avalanche": "A large mass or body of snow and ice sliding swiftly down a mountain side.",
    "mushroom": "Any of the flesh fruiting bodies of fungi typically produced above ground on soil or on their food sources",
    "ferment": "To react; especially to produce alcohol by aging or by allowing yeast to act on sugars",
    "mathematics": "An abstract representational system studying numbers, shapes, structures, quantitative change and relationships between them.",
    "sculpture": "A three-dimensional work of art",
    "ambience": "A particular mood or atmosphere of an environment.",
    "everest": "A very tall mountain.",
    "pineapple": "A sweet yellow fruit with spiky hair.",
    "elephant": "It's got a trunk with a lot of space.",
    "finance": "Money or other assets."
}

def game():
    name = input("Hello! What's your name? ").title()
    if name.isalpha():
        print(f"Welcome to PEEK-A-WORD game {name}! Think you can guess the word I'm thinking of? ")
        print("Type e to start and q to quit.")
        choice = input("Enter choice: ")
        if choice.isalpha() and choice.lower() == "e":
            while True:
                word = random.choice(list(words.keys()))
                turns = len(word) + 6
                guesses = ""
                print(f"The word is {len(word)} letters long.")
                while turns > 0:
                    display_word = ""
                    for char in word:
                        if char in guesses:
                            display_word += char + " "
                        else:
                            display_word += "_ "
                    print(display_word)
                    if display_word.replace(" ", "") == word:
                        print("Hurray! You win!")
                        print(f"The word is: {word.title()}")
                        break
                    guess = input("Enter a letter or type 'hint' for a hint: ").strip().lower()
                    if guess == "hint":
                        print(f"Hint: {words[word]}")
                        turns -= 1
                    elif len(guess) == 1 and guess.isalpha():
                        guesses += guess
                        if guess not in word:
                            turns -= 1
                            print("Incorrect guess!")
                    else:
                        print("You can only guess one letter at a time.")
                    print(f"You have {turns} attempts left.")
                if turns == 0:
                    print("You loose!")
                    print(f"The word was: {word.title()}")
                option = input("Play again(yes/no)? ").strip().lower()
                if option == 'yes':
                    continue
                elif option == 'no':
                    print("Exiting now. Bye!")
                    break
                else:
                    print("Please enter a valid option.")
        else:
            print(f"Aww that's sad. See you next time {name}.")
    else:
        print("Invalid choice.")

game()