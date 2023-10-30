import random
options = ["Rock", "Paper", "Scissors"]
while True:
    user_choice = eval(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    computer_choice = random.choice(options)
    print("You chose : ", user_choice)
    print("Computer chose :", computer_choice)
    if user_choice == computer_choice:
      print("It's tie")
    elif user_choice == 0 and computer_choice == 2:
      print("You win")
    elif user_choice == 1 and computer_choice == 0:
      print("You win")
    elif user_choice == 2 and computer_choice == 1:
      print("You win")
    else:
      print("Computer wins")


    print("Do you want to play again? (Y/N)")
    ans = input().lower
    if ans == 'n':
      break
    
    
