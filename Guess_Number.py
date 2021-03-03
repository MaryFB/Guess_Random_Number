import random
num_of_attempts= []
def display_score():
    if len(num_of_attempts) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(num_of_attempts)))
def game_on():
    random_number = int(random.randint(1, 10))
    print("Hi! Welcome to the game of guesses!")
    player_name = input("Please enter your name: ")
    ask_to_play = input("Hi, {}, would you like to play the guessing number? (Enter Yes/No) ".format(player_name))
    attempts = 0
    display_score()
    while ask_to_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                num_of_attempts.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to play again? (Enter Yes/No) ")
                attempts = 0
                display_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("cool, have a good day!")
                    break
            elif int(guess) > random_number:
                print("The number is lower")
                attempts += 1
            elif int(guess) < random_number:
                print("The number is higher")
                attempts += 1
        except ValueError as err:
            print("Please try a valid value")
            print("({})".format(err))
    else:
        print("cool, have a good day!")
if __name__ == '__main__':
    game_on()
