import random

logo = """   ___                  _   _          _  _            _             
  / __|_  _ ___ ______ | |_| |_  ___  | \| |_  _ _ __ | |__  ___ _ _ 
 | (_ | || / -_|_-<_-< |  _| ' \/ -_) | .` | || | '  \| '_ \/ -_) '_|
  \___|\_,_\___/__/__/  \__|_||_\___| |_|\_|\_,_|_|_|_|_.__/\___|_|  
                                                                     """
print(logo)
start = input("'Start' to play game: ").lower()
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
remaining = True
lives_hard = 5
lives_easy = 10
Num = random.randint(1,100)
while (start == "start" and remaining):

    if difficulty == "hard":
        if lives_hard == 0 :
            print("You ran out of lives, You loose")
            remaining = False
            continue
        print(f"You have {lives_hard} attempts remaining to guess the number")
        guess = input("Make a guess: ")
        if not guess.isnumeric():
            print("Invalid input...")
            guess = input("Make a guess: ")
        guess = int(guess)
        if guess > Num:
            print("Guess too high")
            lives_hard = lives_hard - 1
        elif guess < Num :
            print("Guess too low")
            lives_hard = lives_hard - 1
        else:
            print(f"You got it, The answer was {Num}")
            remaining = False
            continue
    elif difficulty == "easy":
        if lives_easy == 0 :
            print("You ran out of lives, You loose")
            remaining = False
            continue
        print(f"You have {lives_easy} attempts remaining to guess the number")
        guess = input("Make a guess: ")
        if not guess.isnumeric():
            print("Invalid input...")
            guess = input("Make a guess: ")
        guess = int(guess)
        if guess > Num:
            print("Guess too high")
            lives_easy = lives_easy - 1
        elif guess < Num :
            print("Guess too low")
            lives_easy = lives_easy - 1
        else:
            print(f"You got it, The answer was {Num}")
            remaining = False
            continue
    elif difficulty != "hard" or difficulty != "easy":
        print("invalid input....")
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()