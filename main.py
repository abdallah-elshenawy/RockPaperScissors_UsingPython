import random

print("Welcome to the Rock, Paper, Scissors game: ")
choice = input("Press enter to continue or type (Help) for the rules: ").lower()
if (choice == "help"):
   print("\n\t\t********** RULES **********")
   print("\t\t1) You choose and the computer chooses")
   print("\t\t2) Rock smashes Scissors -> Rock wins")
   print("\t\t3) Scissors cut Paper -> Scissors win")
   print("\t\t4) Paper covers Rock -> Paper win\n")

list = ["Rock", "Paper", "Scissors"]
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""
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
user_choice = input("Enter Your choice (rock, paper, scissors): ").capitalize()

if (user_choice in list):

   # user choice
   if (user_choice == "Rock"):
      print(f"\nYou chose: {rock}")
   elif (user_choice == "Paper"):
      print(f"\nYou chose: {paper}")
   else:
      print(f"\nYou chose: {scissors}")

   # computer choice
   rand_int = random.randint(0, 2)
   computer_choice = list[rand_int]
   if (computer_choice == "Rock"):
      print(f"Computer chose: {rock}")
   elif (computer_choice == "Paper"):
      print(f"Computer chose: {paper}")
   else:
      print(f"Computer chose: {scissors}")

   # Determine the winner
   if (user_choice == computer_choice):
      print("We are equivalent !")
   elif (
      (user_choice == "Rock") and (computer_choice == "Paper")
      or 
      (user_choice == "Paper") and (computer_choice == "Scissors")
      or 
      (user_choice == "Scissors") and (computer_choice == "Rock")
   ):
      print(f"You lose, {computer_choice} beats {user_choice}")
   else:
      print(f"You win, {user_choice} beats {computer_choice}")
else: 
   print("Invalid input. Please run the progrm again and choose rock, paper, or scissors.")
