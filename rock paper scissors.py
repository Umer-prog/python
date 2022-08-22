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

import random
print("welcome to the game enter 0 For rock, 1 for paper, 2 for scissors")
user = int(input("Enter you number:"))
if user  == 0:
  print(rock)
elif user == 1:
  print(paper)
elif user == 2:
  print(scissors)
print("Computer choose")
computer = random.randint(0,2)
if computer  == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)
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