import random

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
game_rock=[rock,paper,scissors]
player1 =int(input("What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors: "))

computer = random.randint(0,2)
if 0<= player1 <3:
     print(game_rock[player1])
print(f"Computer choose:{game_rock[computer]}" )

if player1 == computer:
    print("Draw")
elif (player1 == 0  and computer == 2) or (player1 == 2  and computer == 1) or (player1 == 1  and computer == 0):
    print("You win")

else:
    print("Computer Win")