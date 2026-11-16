# Welcome To The Rock Paper Scissors Game 
import random

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Game_img = [rock,paper,scissors]
user_choice = int(input("What do you want to choose ? Type 0 for Rock , 1  for Paper and 2 for Scissors\n"))

if user_choice >= 0 and user_choice <= 2:
    print("user choice :\n")
    print(Game_img[user_choice])

computer_choice = random.randint(0,2)
print("Computer choice :\n")
print(Game_img[computer_choice])


if user_choice >=3 or user_choice < 0:
    print("Invalid number you should choose correct number\n")
elif computer_choice == 0 and user_choice == 2 :
    print("you lose!")
elif computer_choice > user_choice :
    print("you lose!")

elif user_choice == 0  and computer_choice == 2:
    print("you lose!")
elif computer_choice == user_choice :
    print("Game Draw")
