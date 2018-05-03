# A game for guessing a number
# 4/11/18
# CTI-110 P5HW2 - Random Number Guessing Game
# William Buckwell

import random

def main():
    # Varaible used to control the loop
    play = 'Y'

    # Loops the game as long as the varaibel is Y or y
    while play == 'Y' or play == 'y':

        # Start the game
        playGame()
        
        # Determine if they want to play again
        play = input('Would you like to play again? Y/N: ')

def playGame():

    # varaibles to hole the number, control the game loop, and number of guesses
    number = random.randint(1, 100)
    correctAnswer = 'N'
    count = 0

    # loop the game until the number is guessed correctly
    while correctAnswer == 'N':
        guess = int(input('Guess a number between 1 and 100: '))

        if guess > number:
            print('Your guess is to high!')
            count += 1
        elif guess < number:
            print('Your guess is to low!')
            count += 1
        else:
            print('Great job you were right!!')
            print('It took ' + str(count) + ' guesses to get it right!')
            correctAnswer = 'Y'

main()
    
    
