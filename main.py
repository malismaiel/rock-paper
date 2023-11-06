# Define three strings representing images for rock, paper, and scissors.
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

# Create a list containing the images for the three choices.
game_images = [rock, paper, scissors]

# Prompt the user to make a choice (0 for Rock, 1 for Paper, or 2 for Scissors).
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Check if the user's choice is valid (0, 1, or 2) and provide feedback if it's not.
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    # Print the image corresponding to the user's choice.
    print(game_images[user_choice])

    # Generate a random choice for the computer (0 for Rock, 1 for Paper, or 2 for Scissors).
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    # Print the image corresponding to the computer's choice.
    print(game_images[computer_choice])

    # Determine the game outcome based on the user's and computer's choices.
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
