import random

target = random.randint(1,1000)

while True:
    user_choice = (input("Guess the target or Quit(Q):"))
    if (user_choice == "Q" or user_choice == "q"):
        break

    user_choice = int(user_choice)
    if (user_choice == target):
        print("Sucess: Correct Guess")
        break
    elif (user_choice < target):
        print("Your choice is small, Try Again!")
    else:
        print("Your choice is big, Try Again!")

print("------------Game Over------------")