import random

# using global variables
MIN = 1
MAX = 25
win_num = random.choice(range(MIN, MAX))
guess_count = 1
max_guesses = 5
max_guesses1 = 6
bonus = False
you_win = False

print(f"Guess the number between {MIN} and {MAX}. You have {max_guesses} guesses.")
# beginning
while guess_count <= max_guesses:
    guess = int(input(f"[enter a # from {MIN}-{MAX}]: "))
    print(f"Your current guess is {guess}. You are on guess # {guess_count} of {max_guesses}")
    guess_count +=1
    if guess != win_num:
        print("Try again!")
    # elif guess_count == max_guesses:
    #     print("GAME OVER!")
# #+/- 3 it tells you are close 
    if int(win_num - guess) <=3:
        print("You are close!")
# if you guess the correct number wthin 5 guesses you win the game and game breaks 
        
    if guess == win_num:
        print("You have won the game. Thanks for playing. Goodbye!")
        break

# paramiters 
    if int(guess) < MIN or int(guess) > MAX:
        print("Your guess is not within parameters, please try again.")
        guess_count -= 1

    if guess_count == max_guesses1:
        print("GAME OVER!")