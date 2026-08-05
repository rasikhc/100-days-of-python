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

rps = [rock, paper, scissors]
names = ["rock", "paper", "scissors"]
player_1_pick = int(input("rock, paper, scissors:"))
player_1 = rps[player_1_pick]
print(player_1)

computer = random.choice(rps)
print(computer)

if player_1 == rock and computer == scissors:
    print("You win!")
elif player_1 == rock and computer == paper:
    print("You lose!")
elif player_1 == scissors and computer == paper:
    print("You Win!")
elif player_1 == scissors and computer == rock:
    print("You lose!")
elif player_1 == paper and computer == rock:
    print("You Win!")
elif player_1 == paper and computer == scissors:
    print("You lose!")
else:
    print("It's a draw!")