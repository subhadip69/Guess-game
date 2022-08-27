import random

computer_guess = random.randint(1,10)

i = 0 
guess_score = 0


while i != computer_guess:
    user_input = int(input("Enter Your number: "))
    i = user_input
    guess_score += 1

    if user_input > computer_guess:
        print("please Enter a low value: ")
    elif user_input < computer_guess:
        print("please Enter a large value: ")
    else:
        print("Win")

print(f"Your score is {guess_score} ")
