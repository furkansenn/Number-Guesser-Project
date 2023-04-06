import random

my_top_number = input("Please type a number: ")

if my_top_number.isdigit():
    my_top_number = int(my_top_number)

    if my_top_number < 0 :
        print("Please type a positive number than next time!")
        quit()
else:
    print("Please type a number!")
    quit()

random_num = random.randint(0,my_top_number)

guesses = 0

while True:
    guesses += 1
    my_guess = input("Make a guess: ")
    if my_guess.isdigit():
        my_guess= int(my_guess)
    else:
        print("Please type a number next time!")
        continue
    
    if my_guess == random_num:
        print("Congrulations, you did it :) ")
        break
    elif my_guess > random_num: 
        print("Your guess is bigger than random number")
    else:
        print("Your guess is lower than random number")
print("You made it in",guesses,"guesses")
