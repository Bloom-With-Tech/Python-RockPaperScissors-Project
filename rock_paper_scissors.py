# Imports the Python random library, we'll use this later on for the computer's choice
import random

# Declares variables to keep track of user and computer wins
user_wins = 0
computer_wins = 0

# Creates an infinite loop by saying the condition will always be true
while True:
    # Asks for the user's input on the terminal and converts it to lowercase
    user_choice = input('Choose between rock, paper, and scissors. If you want to stop playing, say stop.').lower()
    
    # Checks if the user wants to stop playing
    if user_choice == 'stop':
        # Breaks out of the loop. The code after this will not be ran if the condition is met.
        break

    # Checks if the user typed something that wasn't one of our options
    if user_choice not in ['rock', 'paper', 'scissors']:
        # Tells the user their input was not one of the options
        print('You typed ' + user_choice + '. Please select one of the options' )
        # Moves on with the next iteration and reruns the code in the while loop until the user inputs one of the options
        continue

    # Generates a random integer between 0 and 2
    computer_choice = random.randint(0, 2)
    computer_choice = ['rock', 'paper', 'scissors'][computer_choice]

    # Defines a variable to know the results of the match
    result = ''

    # Checks if you tied
    if computer_choice == user_choice:
        result = 'You tied!'
    # Runs if you didn't ties
    else:
        if computer_choice == 'rock':
            if user_choice == 'scissors':
                result = 'The computer got a point.'
                computer_wins += 1
            elif user_choice == 'paper': 
                result = 'You got a point!'
                user_wins += 1
        elif computer_choice == 'paper':
            if user_choice == 'rock':
                result = 'The computer got a point.'
                computer_wins += 1
            elif user_choice == 'scissors': 
                result = 'You got a point!'
                user_wins += 1
        else:
            if user_choice == 'paper':
                result = 'The computer got a point.'
                computer_wins += 1
            elif user_choice == 'rock': 
                result = 'You got a point!'
                user_wins += 1

    # Tell the user what the result was
    print(result + ' You chose ' + user_choice + ' and the computer chose ' + computer_choice + '.')

    # Tells the user how well they're doing
    print('You won ' + str(user_wins) + ' times. The computer won ' + str(computer_wins) + ' times.')

    # Get the percentage of times the user won. Note: the str() function converts other data types to strings
    try:
        percentage_won = str(user_wins /( computer_wins + user_wins) * 100) + '%'
        print('That puts you at a ' + str(percentage_won) + ' win rate.')
    except:
        print('Play again :)')

print("You're out of the loop")