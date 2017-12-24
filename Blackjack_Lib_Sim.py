"""
Blackjack Library
@Rajesh
12/11/2017
"""

'''
Blackjack infrastructure
These functions create the framework from which the game is able to run 
such functions initialize the deck, sum of the value of the hand and
enable the game to identify the winner given the sum of both the player(s)
hand and the dealers hand
'''


# generates a shoe (collection of cards) with 4 identically decks for the user
def gen_deck():
    deck = []
    num_of_decks = 4

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = {'A': 1,
             '2': 2,
             '3': 3,
             '4': 3,
             '5': 5,
             '6': 6,
             '7': 7,
             '8': 8,
             '9': 9,
             '10': 10,
             'J': 10,
             'Q': 10,
             'K': 10}

    for suit in suits:
        for rank in ranks:
            deck.append(str(rank) + " " + suit)
    return deck * num_of_decks


# iterates the total hand of the player to then be used in the sum (only useful values no suits)
# input the player's or dealers hand
# ouput the numerical hand 
def int_card(some_list):
    indexed = []
    for x in some_list:
        for letter in x:
            if is_int(letter) == True or letter == 'K' or letter == 'J' or letter == 'Q' or letter == 'A':
                indexed.append(letter)
    return indexed


# Returns the sum of each hand as specified ( I made A = 11 for natural 21)
# input the numerical hand of the player's had to produce a total sum
# ouput produces the total sum of a given hand
def sum_hand(card_itter):
    sums = 0
    ray = card_itter
    for x in ray:
        if x == 'K' or x == 'J' or x == 'Q':
            x = 10
            sums += int(x)
        elif x == '0':
            x = 9
            sums += int(x)
        elif x == 'A':
            x = 11
            sums += int(x)
        else:
            sums += int(x)

    return sums


# Forces the dealer to draw until his sum is greater than or equal to 17 
def d_sev(draw_func):
    new = draw_func
    dealer_sum = (sum_hand(int_card(new)))
    return dealer_sum


# declares blackjack per initial draw by the user (first serve)          
def win_check(sum_total):
    if sum_total == 21:
        return 2
    elif sum_total > 21:
        return -1


# runs through the available hand sums to find the winner
# input the players sum as well as 
# ouput a numerical value that corresponds to a win, loss or a neutral state
def find_winner(p_sum, d_sum):
    if d_sum < p_sum <= 21:
        return 1
    elif p_sum < d_sum <= 21:
        return -1
    elif p_sum == d_sum:
        return 0
    elif p_sum > 21 and d_sum > 21:
        return 0
    elif p_sum > 21 >= d_sum:
        return -1
    elif d_sum > 21 >= p_sum:
        return 1


# check to see whehter to add or subtract value of bet from the funds
# input a numerical value, the players funds as well as the bet size
# ouput the resulting addition or subtraction of value from total funds
def bet_check(value, funds, bet):
    if value == 1:
        funds += bet
        return funds
    elif value == -1:
        funds -= bet
        return funds
    elif value == 0:
        funds += 0
        return funds


'''
Blackjack Functionality 
Create the functionality of the player, including the right to double, split
and take out insurance in accordance to the hands that are present
'''


# double bets and returns either 0 or doubles your initial bet
# input inclue the bet amount, the players total funds and the state of leverage
# output doubles the bet in accordance to players leverage constraints 
def double(bet, funds, lev):
    double = bet * 2
    
    if lev:
        return double
    if not lev:
        if double <= funds:
            return double
        else:
            return 0


# split your and and allows you to play separate hands each
# inputs include the players hand and the players numerical hand (only value faces and high cards without suit)
# outputs the a new list that appens each card from the two deal intial hand seperatley
def split(some_list, original_list):
    empty = []
    if some_list[0] == some_list[1]:
        for x in original_list:
            empty.append([x])
        return empty
    else:
        return 0


# take out insurance in the event the dealer is showing a high card
# inputs inlcude the dealers hands, the available funds of the player and their desired side bet
# outputs the side bet or 0 in the event of no 'A' show
def insurance(some_list, funds, insurance_bet):
    show = some_list[0]
    if show == 'A':
        if insurance_bet < funds:
            side_bet = insurance_bet
            return side_bet
    else:
        return 0
   

'''
Case Checking
These functions are responsible for case checking user input such as integer,
character etc:
'''


# case checks integers for a given input of strings
# this function is used as a back channel program that assits others
def is_int(some_string):
    try:
        float(some_string)
    except ValueError:
        return False
    return True
