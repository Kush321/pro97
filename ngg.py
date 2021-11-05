import random
number = random.randint(0,10)
chances = 5
while chances > 0:
    guess = int(input("Input your guess: "))
    if guess == number:
        print("")
        print("CONGRATULATIONS YOU WON!!!")
        chances = -2
    elif guess < number:
        print("Your guess is too low!")
        print("")
        chances = chances-1
    elif guess > number:
        print("Your guess is too high!")
        print("")
        chances = chances-1
if chances == 0:
    print("")
    print("YOU LOSE!!! The number is ", number)