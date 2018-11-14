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
import numpy
import pandas as pd


def gen_deck(deck_num: int):
    """
    Generates a shoe (collection of cards) with 4 identically decks for the user, where suits don't matter
    :param deck_num:
    :return:
    """

    deck = []
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in range(0, 4):
        for rank in ranks:
            deck.append('{}'.format(rank))
    big_deck = deck * deck_num
    random.shuffle(big_deck)
    return big_deck


def sum_hand(card_values: list):
    """
    Calculates the sum of each hand as specified
    :param card_values:
    :return:
    """

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


def dealer_serve(draw_func, dealers_hand: list):
    """
    Forces the dealer to draw until his sum is greater than or equal to 17
    :param draw_func:
    :param dealers_hand:
    :return:
    """

    assert callable(draw_func) is True, 'Variable must be a function'
    dealer_sum = sum_hand(dealers_hand)
    if dealer_sum < 17:
        while dealer_sum < 17:
            dealers_hand = draw_func(dealers_hand)
            dealer_sum = sum_hand(dealers_hand)
    return dealers_hand


def find_winner(player_sum: int, dealer_sum: int):
    """
    Runs through the available hand sums to find the winner (1) you win, (-1) dealer wins (0) draw between dealer
    :param player_sum:
    :param dealer_sum:
    :return:
    """

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


def bet_check(value: int, funds: int, bet: int):
    """
    Check to see whether to add or subtract value of bet from the funds
    :param value:
    :param funds:
    :param bet:
    :return:
    """

    if value == 1:
        funds += bet
        return funds
    elif value == -1:
        funds -= bet
        return funds
    elif value == 0:
        funds += 0
        return funds


def double_func(bet: int, funds: int):
    """
    Double bets and returns either 0 or doubles your initial bet, leverage and available funds
    :param bet:
    :param funds:
    :return:
    """

    doubler = bet * 2
    if doubler <= funds:
        return doubler
    else:
        return 0


def insurance_func(dealer_list: list, funds: int, insurance_bet: int):
    """
    Take out insurance in the event the dealer is showing a high card
    :param dealer_list:
    :param funds:
    :param insurance_bet:
    :return:
    """

    show_card = dealer_list[0]
    if show_card == 'A':
        if insurance_bet < funds:
            return insurance_bet


class Game:

    def __init__(self, bet: int, funds: int, side_bet: int = 0, deck_num: int = 4, split: bool = True,
                 insurance: bool = False, double: bool = True):
        """
        Initializes the game with predefined arguments regarding game structure
        :param bet: determines the size of initial and subsequent bets (type integer)
        :param funds: determines starting funds for the game (type integer)
        :param side_bet: determines the size of side_bet in the event of insurance (type integer)
        :param deck_num: determines the number of playable decks for the game
        :param split: indicates the player's preference to split if available (type bool)
        :param insurance: indicates the player's preference to take out insurance if available (type bool)
        :param double: indicates the player's preference to double if available (type bool)
        """

        assert bet < funds, "The value of your bet exceeds your total funds"

        self.deck_num = deck_num
        self.deck = gen_deck(deck_num=self.deck_num)
        self.reshuffle_threshold = len(self.deck) - round(len(self.deck) / 3)

        self.bet = bet
        self.funds = funds
        self.split = split
        self.insurance = insurance
        self.double = double
        self.side_bet = side_bet

        numpy.random.shuffle(self.deck)

    def _hit_(self, some_list: list):
        """
        Hit functionality for another card to be drawn for the user
        :param some_list: referencing the player/dealer hands
        :return: a new list with an additional card added
        """

        new_card = self.deck.pop()
        some_list.append(new_card)
        return some_list

    def _sequence_(self, players_hand: list, dealer_hand: list, bet: int):
        """
        Executes a typical game structure following initial betting round to find a winner
        :param players_hand: a list of the players cards
        :param dealer_hand: a list of the dealers cards after standing on iterative 17
        :param bet: the amount the player is betting per round
        :return: the updated value of playable funds
        """

        new_p_sum = sum_hand(card_values=players_hand)
        new_d_sum = sum_hand(card_values=dealer_hand)

        val = find_winner(player_sum=new_p_sum, dealer_sum=new_d_sum)
        self.funds = bet_check(value=val, funds=self.funds, bet=bet)
        return self.funds

    def _split_(self, card_list: list):
        """
        Splits the players cards if they happen to contain the same face value card
        :param card_list: the players cards expressed as a list
        :return: a new list of length 2 with two lists within each element => [['K','2'],['K','10']]
        """

        empty = []
        if card_list[0] == card_list[1]:
            for card in card_list:
                empty.append([card, self.deck.pop()])
        return empty

    def starting_serve(self):
        """
        Simulates two card draws for both the player and dealer
        :return: two lists, one representing the players 2 card draw and the other for the dealer
        """

        if len(self.deck) < self.reshuffle_threshold:
            self.deck = gen_deck(deck_num=self.deck_num)

        dealers_hand = []
        players_hand = []

        # deals a hand of 2 cards to the player and dealer by popping the last unit of the shuffled list
        for x in range(0, 2):
            dealer_card = self.deck.pop()
            dealers_hand.append(dealer_card)

            player_card = self.deck.pop()
            players_hand.append(player_card)

        return dealers_hand, players_hand

    def blackjack(self, dealers_hand: list= None, players_hand: list=None):
        """
        simulates a game of blackjack as per specification imputed by user
        :return: available funds after successful completion of hand
        """

        if dealers_hand is None and players_hand is None:
            dealers_hand, players_hand = self.starting_serve()

        if self.funds > 0:

            # insurance mechanic if the dealer presents an Ace
            if self.insurance:
                self.side_bet = insurance_func(dealer_list=dealers_hand,
                                               funds=self.funds,
                                               insurance_bet=self.side_bet)

            # returns the sum of player's and the dealer's respective hand value
            d_sum = sum_hand(card_values=dealers_hand)
            p_sum = sum_hand(card_values=players_hand)

            # checks to see if dealer has a natural 21 on the first draw/deal
            if d_sum == 21 and p_sum < 21:
                self.funds -= self.bet
                self.funds += (self.side_bet * 2)

            else:
                # if the dealer does not hit a natural 21 you lose your side bet (insurance)
                self.funds -= self.side_bet

                # if you receive a natural 21 you receive a 3:2 payout and dealer loses
                if p_sum == 21 and d_sum < 21:
                    self.funds += ((self.bet / 2) * 3)

                # if you do not receive a natural 21 then you are asked to hit, stand, double or split
                else:
                    strategy_df = pd.read_csv('blackjack_basic_strategy.csv')
                    strategy_df = strategy_df.set_index('Players Hand')
                    player_ref = ','.join(players_hand)
                    hole_card = dealers_hand.pop()

                    try:
                        action = strategy_df.loc[player_ref].loc[hole_card]
                    except KeyError:
                        action = strategy_df.loc[str(p_sum)].loc[hole_card]

                    final_dealer_hand = dealer_serve(draw_func=self._hit_,
                                                     dealers_hand=dealers_hand)

                    if action == 'H':
                        new_hand = self._hit_(players_hand)
                        self.funds = self._sequence_(players_hand=new_hand,
                                                     dealer_hand=final_dealer_hand,
                                                     bet=self.bet)

                    elif action == 'S':
                        self.funds = self._sequence_(players_hand=players_hand,
                                                     dealer_hand=final_dealer_hand,
                                                     bet=self.bet)

                    elif action == 'SP' and self.split:
                        split_hand = self._split_(card_list=players_hand)
                        for hand in split_hand:
                            self.blackjack(dealers_hand=final_dealer_hand, players_hand=hand)

                    elif action == 'Double' and self.double:
                        bet_amt = double_func(bet=self.bet, funds=self.funds)
                        new_hand = self._hit_(players_hand)
                        self.funds = self._sequence_(players_hand=new_hand,
                                                     dealer_hand=final_dealer_hand,
                                                     bet=bet_amt)

        return self.funds


if __name__ == "__main__":
    test = Game(bet=100, funds=10000)
    test.blackjack()
