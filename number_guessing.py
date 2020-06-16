import random

start = random.randint(1, 90)
end = random.randint(start, 100)
number = random.randint(start, end)

number_of_guesses = 0

def number_guessing(number, guesses):
    
    
    user_guess = input("The computer chose a number between {start} and {end} try to guess it:\n".format(start=start, end=end))

    try:
        if not start <= int(user_guess) <= end:
            print("Please guess a number between the 2 numbers")
            return number_guessing(number, guesses) 
    
    except ValueError:
        print("Please guess a NUMBER between the 2 numbers")
        return number_guessing(number, guesses)

    if int(user_guess) > number:
        print("Your guess was higher than the number guess lower")
        guesses += 1
        return number_guessing(number,guesses)

    elif int(user_guess) < number:
        print("Your guess was lower than the number guess higher")
        guesses += 1
        return number_guessing(number, guesses)
    
    else:
        guesses += 1
        print("Your guess was {user_guess} and the computer number was {number} you win!\nYou did it in {guesses} number of guesses".format(user_guess=user_guess, number=number, guesses=str(guesses)))


number_guessing(number, number_of_guesses)
