import random
Rock = """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice = [Rock, Paper, Scissors]
choice_input = int(input("What do you choose Enter 0 for Rock, 1 for Paper, 2 for Scissors"))
computer_choice = random.randint(0, 2)

if choice_input == 0:
    print("Your choice is", choice[choice_input])
    if computer_choice == 0:
        print("Computer choice is", choice[computer_choice])
        print("Draw")
    elif computer_choice == 1:
        print("Computer choice is", choice[computer_choice])
        print("You Loose")
    else:
        print("Computer choice is", choice[computer_choice])
        print("You won")
elif choice_input == 1:
    print("Your choice is", choice[choice_input])
    if computer_choice == 0:
        print(choice[computer_choice])
        print("You won")
    elif computer_choice == 1:
        print(choice[computer_choice])
        print("Draw")
    else:
        print(choice[computer_choice])
        print("You loose")
else:
    print("Your choice is", choice[choice_input])
    if computer_choice == 0:
        print(choice[computer_choice])
        print("You loose")
    elif computer_choice == 1:
        print(choice[computer_choice])
        print("You won")
    else:
        print(choice[computer_choice])
        print("Draw")
        
