##################################################

"""
==========================================
Author: Rajesh Rao
Licensed for public use
All Rights Reserved
==========================================
"""

##################################################
# Import Libraries and modules
##################################################
import pandas as pd
import numpy as np


def gen_deck(deck_num: int):
    """
    Generates a shoe (collection of cards) with 4 identically decks for the user, where suits don't matter
    :param deck_num: the number of decks to generate for the user
    :return: a list of shuffled decks for the user
    """

    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = np.array([i for _ in range(0, 4 * deck_num) for i in ranks], str)
    np.random.shuffle(deck)
    return deck


def sum_hand(card_values: np.array):
    """
    Calculates the sum of each hand as specified
    :param card_values: provide a list containing the face value of given cards
    :return: returns the sum of card values defined by standard blackjack rules
    """

    card_sum = 0
    for card in card_values:
        if card == 'K' or card == 'J' or card == 'Q':
            card_sum += 10
        elif card == 'A':
            if card_sum < 11:
                card_sum += 11
            else:
                card_sum += 1
        else:
            card_sum += int(card)
    return card_sum


def dealer_serve(draw_func, dealers_hand: np.array):
    """
    Forces the dealer to draw until his sum is greater than or equal to 17
    :param draw_func: provided function to simulate draw/hit for dealer
    :param dealers_hand: a list of card values assigned to the dealer
    :return: returns a new dealer list with updated cards appended to the original list
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
    :param player_sum: the value of the players hand
    :param dealer_sum: the value of the dealers hand
    :return: an integer from the set of [-1, 0, 1] indicating [loss, draw, win]
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
    :param value: the value which corresponds to the find_winner function
    :param funds: the amount of funds available specified by the player
    :param bet: the original bet amount specified by the player
    :return: the new funds amount according to win/loss value
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
    :param bet: the original bet amount specified by the player
    :param funds: the amount of funds available specified by the player
    :return: returns the new defined bet amount
    """

    doubler = bet * 2
    if doubler <= funds:
        return doubler
    else:
        return bet


def insurance_func(dealer_list: np.array, funds: int, insurance_bet: int):
    """
    Take out insurance in the event the dealer is showing a high card
    :param dealer_list: a list of card values assigned to the dealer
    :param funds: the amount of funds available specified by the player
    :param insurance_bet: specified insurance bet by user
    :return: returns the insurance bet as specified by the user
    """

    show_card = dealer_list[0]
    if show_card == 'A':
        if insurance_bet < funds:
            return insurance_bet


class Game:

    def __init__(self, bet: int, funds: int, side_bet: int = 0, deck_num: int = 4, split: bool = True,
                 insurance: bool = False, double: bool = True, card_counter: str=None):
        """
        Initializes the game with predefined arguments regarding game structure
        :param bet: determines the size of initial and subsequent bets (type integer)
        :param funds: determines starting funds for the game (type integer)
        :param side_bet: determines the size of side_bet in the event of insurance (type integer)
        :param deck_num: determines the number of playable decks for the game
        :param split: indicates the player's preference to split if available (type bool)
        :param insurance: indicates the player's preference to take out insurance if available (type bool)
        :param double: indicates the player's preference to double if available (type bool)
        :param card_counter: optional strategy specifying card counting strategy(type str)
        """

        assert bet < funds, "The value of your bet exceeds your total funds"

        self.deck_num = deck_num
        self.deck = gen_deck(deck_num=self.deck_num)
        self.reshuffle_threshold = round(len(self.deck)*.75)

        self.bet = bet
        self.funds = funds
        self.split = split
        self.insurance = insurance
        self.double = double
        self.side_bet = side_bet

        self.card_counter = card_counter
        self.cards_played = np.array([])

    def _hit_(self, some_list: np.array):
        """
        Hit functionality for another card to be drawn for the user
        :param some_list: referencing the player/dealer hands
        :return: a new list with an additional card added
        """

        self.deck, new_card = self.deck[:-1], self.deck[-1]
        some_list = np.append(some_list, new_card)
        return some_list

    def _sequence_(self, players_hand: np.array, dealer_hand: np.array, bet: int):
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
        funds = bet_check(value=val, funds=self.funds, bet=bet)
        return funds

    def _split_(self, card_list: np.array):
        """
        Splits the players cards if they happen to contain the same face value card
        :param card_list: the players cards expressed as a list
        :return: a new list of length 2 with two lists within each element => [['K','2'],['K','10']]
        """

        empty = np.array([])
        if card_list[0] == card_list[1]:
            for card in card_list:
                self.deck, new_card = self.deck[:-1], self.deck[-1]
                empty = np.append(empty, [card, new_card])
        return empty

    def _starting_serve_(self):
        """
        Simulates two card draws for both the player and dealer
        :return: two lists, one representing the players 2 card draw and the other for the dealer
        """

        if len(self.deck) < self.reshuffle_threshold:
            self.deck = gen_deck(deck_num=self.deck_num)

        dealers_hand = np.array([])
        players_hand = np.array([])

        # deals a hand of 2 cards to the player and dealer by popping the last unit of the shuffled list
        for _ in range(0, 2):
            self.deck, dealer_card = self.deck[:-1], self.deck[-1]
            dealers_hand = np.append(dealers_hand, dealer_card)

            self.deck, player_card = self.deck[:-1], self.deck[-1]
            players_hand = np.append(players_hand, player_card)

        return dealers_hand, players_hand

    def _scaler_(self):
        count_strategy_df = pd.read_csv('card_count_strategy.csv')
        count_strategy_df = count_strategy_df.set_index('Card Counting Strategies')

        rule_set = count_strategy_df.loc[self.card_counter]
        return sum([rule_set.loc[card] for card in self.cards_played])

    def blackjack(self, dealers_hand: np.array= None, players_hand: np.array=None):
        """
        simulates a game of blackjack as per specification imputed by user
        :return: available funds after successful completion of hand
        """

        if dealers_hand is None or players_hand is None:
            dealers_hand, players_hand = self._starting_serve_()

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
                elif p_sum == 21 and d_sum == 21:
                    pass

                # if you do not receive a natural 21 then you are asked to hit, stand, double or split
                else:
                    strategy_df = pd.read_csv('blackjack_basic_strategy.csv')
                    strategy_df = strategy_df.set_index('Players Hand')
                    player_ref = ','.join(players_hand)
                    swap_player_ref = '{le},{rg}'.format(le=player_ref[2],
                                                         rg=player_ref[0])
                    hole_card = dealers_hand[0]

                    if player_ref in strategy_df.index:
                        action = strategy_df.loc[player_ref].loc[hole_card]
                    elif swap_player_ref in strategy_df.index:
                        action = strategy_df.loc[swap_player_ref].loc[hole_card]
                    else:
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
                        for card in range(0, len(split_hand), 2):
                            new_player_hand = split_hand[card:card + 2]
                            self.blackjack(dealers_hand=final_dealer_hand, players_hand=new_player_hand)

                    elif action == 'Double' and self.double:
                        bet_amt = double_func(bet=self.bet, funds=self.funds)
                        new_hand = self._hit_(players_hand)
                        self.funds = self._sequence_(players_hand=new_hand,
                                                     dealer_hand=final_dealer_hand,
                                                     bet=bet_amt)

                    self.cards_played = np.append(self.cards_played, final_dealer_hand)

        return self.funds, self.bet


if __name__ == "__main__":
    import time
    t1 = time.process_time()
    g = Game(bet=100, funds=10000, card_counter='Hi-Lo')
    # print(g.blackjack(dealers_hand=np.array(['6', '7']),
    #                   players_hand=np.array(['8', '8'])))
    print(g._scaler_())
    print(t1-time.process_time())
