# craps.py
#
# This program simulates the dice game craps. The user starts with $100 and is allowed to bet on the roll of two
# six-sided dice:
#
#  - A roll of 7 or 11 on the opening throw results in a win
#  - A roll of 2, 3, or 12 on the opening throw results in a loss
#  - A roll of anything else means the user has to re-roll the dice until that same number is rolled (a win) or a 7 is
#    rolled (a loss)
#
# A win pays whatever amount was bet. A loss takes the amount bet. The user can continue to play until he/she is out of
# money.
#
# by Mr. Ciccolo

import random
totalwinnings = 100
bet = 0
def main():
    global totalwinnings
    global bet
    display_welcome()
    play_again = True
    while play_again == True:
        playerbet()
        total = roll_dice()
        if total == 7 or total == 11:
            print("You win!")
            totalwinnings = totalwinnings + bet
            print("Your current balance is $", totalwinnings)
        elif total == 2 or total == 3 or total == 12:
            print("You lose!")
            totalwinnings = totalwinnings - bet
            print("Your current balance is $", totalwinnings)
        else:
            re_roll(total)
        print() # Blank line for spacing
        if totalwinnings > 5:
            play_again_n = "x"
            while play_again_n == "x":
                play_again_n = (input("Press enter to play another round or n to keep your money"))
                if play_again_n == "n" :
                    print("Congrats, you left the game without losing it all. You left with $", totalwinnings)
                    play_again = False
                if play_again_n == "":
                    play_again = True
                else:
                    play_again_n = "x"
            clear_screen()
        if totalwinnings == 0:
            print("Ya broke, get out!")
            play_again = False
        elif totalwinnings < 5:
            print("Ya done, you can't be here with only $", totalwinnings)
            play_again = False

def playerbet():
    global bet
    global totalwinnings
    bet = 0
    while bet == 0:
        bet = eval(input("You have $%s How much would you like to bet" % totalwinnings))
        if bet == "":
            print("Please place a bet")
            print("")
        if bet >= 5 and bet <= totalwinnings:
            print("")
        elif bet < 5:
            print("Don't be weak, you have to bet at least $5")
            bet = 0
            print("")
        else:
            print("I aint stupid, you don't have $", bet, "to bet!")
            bet = 0
            print("")
    return bet
def clear_screen():
    for i in range(20):
        print()


def display_welcome():
    global totalwinnings
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$                                              $")
    print("$ Welcome to the Computer Science Craps Table! $")
    print("$                                              $")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()

def roll_dice():
    global bet
    input("Press Enter to roll the dice... $%s is on the line" %bet) # We don't do anything with the input, we're just using it to pause the game

    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    total = die1 + die2

    print()
    print(" +---+   +---+")
    print(" |", die1, "| + |", die2, "| =", total)
    print(" +---+   +---+")
    print()

    return total


def re_roll(point):
    print("You have to keep rolling until you get another", point)
    print() # Blank line for spacing
    global totalwinnings
    global bet
    total = roll_dice()
    while total != point and total != 7:
        total = roll_dice()

    if total == point:
        print("You win!")
        totalwinnings = totalwinnings + bet
        print("Your current balance is $", totalwinnings)
    if total == 7:
        print("You lose!")
        totalwinnings = totalwinnings - bet
        if totalwinnings >= 5:
            print("Your current balance is $", totalwinnings)
    return totalwinnings
main()
