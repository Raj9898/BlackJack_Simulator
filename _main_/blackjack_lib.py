##################################################

"""
==========================================
Author: Rajesh Rao
Licensed for public use
All Rights Reserved
==========================================
"""


#############################################
# Import Libraries and modules
#############################################
import random


# generates a shoe (collection of cards) with 4 identically decks for the user, where suits don't matter
def gen_deck(deck_num: int):
    deck = []

    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    for suit in range(0, 4):
        for rank in ranks:
            deck.append('{}'.format(rank))
    big_deck = deck * deck_num
    random.shuffle(big_deck)
    return big_deck


# Returns the sum of each hand as specified
def sum_hand(card_values: list):
    card_sum = 0

    for card in card_values:
        if card == 'K' or card == 'J' or card == 'Q':
            card_sum += 10
        elif card == 'A':
            if card_sum < 10:
                card_sum += 11
            else:
                card_sum += 1
        else:
            card_sum += int(card)

    return card_sum


# Forces the dealer to draw until his sum is greater than or equal to 17 
def d_sev(draw_func):
    dealer_sum = (sum_hand(draw_func))
    return dealer_sum


# declares blackjack per initial draw by the user (first serve)          
def win_check(sum_total: int):
    if sum_total == 21:
        return 2
    elif sum_total > 21:
        return -1


# runs through the available hand sums to find the winner (1) you win, (-1) dealer wins (0) draw between dealer
def find_winner(player_sum: int, dealer_sum: int):
    if dealer_sum < player_sum <= 21:
        return 1
    elif player_sum < dealer_sum <= 21:
        return -1
    elif player_sum == dealer_sum:
        return 0
    elif player_sum > 21 and dealer_sum > 21:
        return 0
    elif player_sum > 21 >= dealer_sum:
        return -1
    elif dealer_sum > 21 >= player_sum:
        return 1


# check to see whether to add or subtract value of bet from the funds
def bet_check(value: int, funds: int, bet: int):
    if value == 1:
        funds += bet
        return funds
    elif value == -1:
        funds -= bet
        return funds
    elif value == 0:
        funds += 0
        return funds


# double bets and returns either 0 or doubles your initial bet, leverage and available funds
def double(bet: int, funds: int):
    doubler = bet * 2

    if doubler <= funds:
        return doubler
    else:
        return 0


# split your cards allows you to play separate hands each
def split(card_list: list):
    empty = []
    if card_list[0] == card_list[1]:
        for card in card_list:
            empty.append([card])
            return empty


# take out insurance in the event the dealer is showing a high card
def insurance(dealer_list: list, funds: int, insurance_bet: int):
    show_card = dealer_list[0]
    if show_card == 'A':
        if insurance_bet < funds:
            return insurance_bet
