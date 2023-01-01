import random
import sys

# These variables keep track of wins, losses and ties for the player
wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors')
        playermove = input()
        if playermove == 'q':
            sys.exit() #Quit the program
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break  #Break out of the player input loop
        print('Please pick (r)ock, (p)aper, (s)cissors, (q)uit.')
    # Display what the player chose
    if playermove == 'r':
        print('Rock versus...')
    elif playermove == 'p':
        print('Paper versus...')
    elif playermove == 's':
        print('Scissors versus...')

    # Display what the computer chose
    randomnumber = random.randint(1,3)
    if randomnumber == 1:
        computermove = 'r'
        print('Rock')
    elif randomnumber == 2:
        computermove = 'p'
        print('Paper')
    elif randomnumber == 3:
        computermove = 's'
        print('Scissors')

    # Display and record the win/loss/tie:
    if playermove == computermove:
        print("It's a tie!")
        ties = ties + 1
    elif playermove == 'r' and computermove == 'p':
        print('You lose! Skynet is gaining control')
        losses = losses + 1
    elif playermove == 'r' and computermove == 's':
        print('You win! You are helping Sarah Connor defeat Skynet')
        wins = wins + 1
    elif playermove == 'p' and computermove == 's':
        print('You lose! Skynet is gaining control')
        losses = losses + 1
    elif playermove == 'p' and computermove == 'r':
        print('You win! You are helping Sarah Connor defeat Skynet')
        wins = wins + 1
    elif playermove == 's' and computermove == 'r':
        print('You lose! Skynet is gaining control')
        losses = losses + 1
    elif playermove == 's' and computermove == 'p':
        print('You win! You are helping Sarah Connor defeat Skynet')
        wins = wins + 1
