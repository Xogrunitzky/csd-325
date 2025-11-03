"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

#Xavier Grunitzky
#Module 3.2 Assignment
#11/2/25
#Changed code to fit requirements for assignment.

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# New notice: Added notice about 10 mon bonus for 2 or 7
print('''Cho-Han, by Al Sweigart al@inventwithpython.com
In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number. *If the user gets a 2 or a 
7 on a dice roll, they get a 10 mon bonus*.
''')

purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # New code: Input prompt changed to your initials
        pot = input('xog: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break  # Exit loop when valid bet entered

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Player chooses CHO or HAN
    while True:
        bet = input('> ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal dice results
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if roll is even or odd
    rollIsEven = (dice1 + dice2) % 2 == 0
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # Display results
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        # New code: 12% house fee instead of 10%
        houseFee = pot // 12
        print('The house collects a', houseFee, 'mon fee.')
        purse -= houseFee
    else:
        purse -= pot
        print('You lost!')

    # New code: 10 mon bonus for total 2 or 7
    total = dice1 + dice2
    if total == 2 or total == 7:
        print('Bonus! You rolled a', total, 'and earned 10 mon!')
        purse += 10

    # Check if the player has run out of money
    if purse <= 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()