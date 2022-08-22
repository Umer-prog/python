rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
import random

game_sign = [rock, paper, scissors]
print("welcome to the game enter 0 For rock, 1 for paper, 2 for scissors")
user = int(input("Enter you number:"))
if user >= 3 or user < 0:
    print("invalid input")
else:
    print(game_sign[user])
    print("Computer choose")
    computer = random.randint(0, 2)
    print(game_sign[computer])

    if computer == user:
        print("Its a draw...")
    elif computer == 0 and user == 1:
        print("You won")
    elif computer == 0 and user == 2:
        print("You lost")
    elif computer == 1 and user == 0:
        print("you lost")
    elif computer == 1 and user == 2:
        print("You won")
    elif computer == 2 and user == 0:
        print("You won")
    elif computer == 2 and user == 1:
        print("You lost")