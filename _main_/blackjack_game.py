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
import numpy as np

# created through function call pd.read_csv('blackjack_basic_strategy.csv').set_index('Players Hand').to_dict()
basic_strategy_profile = {'2': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'S', '15': 'S',
                                '14': 'S', '13': 'S', '12': 'H', '11': 'D', '10': 'D', '9': 'H', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'S',
                                'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'SP', '7,7': 'SP', '6,6': 'SP', '5,5': 'D',
                                '4,4': 'H', '3,3': 'SP', '2,2': 'SP'},
                          '3': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'S', '15': 'S',
                                '14': 'S', '13': 'S', '12': 'H', '11': 'D', '10': 'D', '9': 'D', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'D',
                                'A,6': 'D', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'SP', '7,7': 'SP', '6,6': 'SP', '5,5': 'D',
                                '4,4': 'H', '3,3': 'SP', '2,2': 'SP'},
                          '4': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'S', '15': 'S',
                                '14': 'S', '13': 'S', '12': 'S', '11': 'D', '10': 'D', '9': 'D', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'D',
                                'A,6': 'D', 'A,5': 'D', 'A,4': 'D', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'SP', '7,7': 'SP', '6,6': 'SP', '5,5': 'D',
                                '4,4': 'H', '3,3': 'SP', '2,2': 'SP'},
                          '5': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'S', '15': 'S',
                                '14': 'S', '13': 'S', '12': 'S', '11': 'D', '10': 'D', '9': 'D', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'D',
                                'A,6': 'D', 'A,5': 'D', 'A,4': 'D', 'A,3': 'D', 'A,2': 'D', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'SP', '7,7': 'SP', '6,6': 'SP', '5,5': 'D',
                                '4,4': 'SP', '3,3': 'SP', '2,2': 'SP'},
                          '6': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'S', '15': 'S',
                                '14': 'S', '13': 'S', '12': 'S', '11': 'D', '10': 'D', '9': 'D', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'D',
                                'A,6': 'D', 'A,5': 'D', 'A,4': 'D', 'A,3': 'D', 'A,2': 'D', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'SP', '7,7': 'SP', '6,6': 'SP', '5,5': 'D',
                                '4,4': 'SP', '3,3': 'SP', '2,2': 'SP'},
                          '7': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'H', '15': 'H',
                                '14': 'H', '13': 'H', '12': 'H', '11': 'D', '10': 'D', '9': 'H', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'S',
                                'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'S', '7,7': 'SP', '6,6': 'H', '5,5': 'D',
                                '4,4': 'H', '3,3': 'SP', '2,2': 'SP'},
                          '8': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'H', '15': 'H',
                                '14': 'H', '13': 'H', '12': 'H', '11': 'D', '10': 'D', '9': 'H', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'S',
                                'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'SP', '7,7': 'H', '6,6': 'H', '5,5': 'D',
                                '4,4': 'H', '3,3': 'H', '2,2': 'H'},
                          '9': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'H', '15': 'H',
                                '14': 'H', '13': 'H', '12': 'H', '11': 'D', '10': 'D', '9': 'H', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'H',
                                'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'SP', '7,7': 'H', '6,6': 'H', '5,5': 'D',
                                '4,4': 'H', '3,3': 'H', '2,2': 'H'},
                          '10': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'H', '15': 'H',
                                 '14': 'H', '13': 'H', '12': 'H', '11': 'D', '10': 'H', '9': 'H', '8': 'H',
                                 '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'H',
                                 'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                 '8,8': 'SP', '10,10': 'S', '9,9': 'S', '7,7': 'H', '6,6': 'H', '5,5': 'H',
                                 '4,4': 'H', '3,3': 'H', '2,2': 'H'},
                          'J': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'H', '15': 'H',
                                '14': 'H', '13': 'H', '12': 'H', '11': 'D', '10': 'H', '9': 'H', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'H',
                                'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'S', '7,7': 'H', '6,6': 'H', '5,5': 'H',
                                '4,4': 'H', '3,3': 'H', '2,2': 'H'},
                          'Q': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'H', '15': 'H',
                                '14': 'H', '13': 'H', '12': 'H', '11': 'D', '10': 'H', '9': 'H', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'H',
                                'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'S', '7,7': 'H', '6,6': 'H', '5,5': 'H',
                                '4,4': 'H', '3,3': 'H', '2,2': 'H'},
                          'K': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'H', '15': 'H',
                                '14': 'H', '13': 'H', '12': 'H', '11': 'D', '10': 'H', '9': 'H', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'H',
                                'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'S', '7,7': 'H', '6,6': 'H', '5,5': 'H',
                                '4,4': 'H', '3,3': 'H', '2,2': 'H'},
                          'A': {'21': 'S', '20': 'S', '19': 'S', '18': 'S', '17': 'S', '16': 'H', '15': 'H',
                                '14': 'H', '13': 'H', '12': 'H', '11': 'H', '10': 'H', '9': 'H', '8': 'H',
                                '7': 'H', '6': 'H', '5': 'H', 'A,10': 'S', 'A,9': 'S', 'A,8': 'S', 'A,7': 'H',
                                'A,6': 'H', 'A,5': 'H', 'A,4': 'H', 'A,3': 'H', 'A,2': 'H', 'A,A': 'SP',
                                '8,8': 'SP', '10,10': 'S', '9,9': 'S', '7,7': 'H', '6,6': 'H', '5,5': 'H',
                                '4,4': 'H', '3,3': 'H', '2,2': 'H'}}

# call pd.read_csv('card_count_strategy.csv').set_index('Card Counting Strategies').transpose().to_dict()
card_counting_profiles = {'Hi-Lo': {'2': 1.0, '3': 1.0, '4': 1.0, '5': 1.0, '6': 1.0, '7': 0.0,
                                    '8': 0.0, '9': 0.0, '10': -1.0, 'J': -1.0, 'Q': -1.0, 'K': -1.0, 'A': -1.0},
                          'Hi-Opt I': {'2': 0.0, '3': 1.0, '4': 1.0, '5': 1.0, '6': 1.0, '7': 0.0,
                                       '8': 0.0, '9': 0.0, '10': -1.0, 'J': -1.0, 'Q': -1.0, 'K': -1.0, 'A': 0.0},
                          'Hi-Opt II': {'2': 1.0, '3': 1.0, '4': 2.0, '5': 2.0, '6': 1.0, '7': 1.0,
                                        '8': 0.0, '9': 0.0, '10': -2.0, 'J': -2.0, 'Q': -2.0, 'K': -2.0, 'A': 0.0},
                          'KO': {'2': 1.0, '3': 1.0, '4': 1.0, '5': 1.0, '6': 1.0, '7': 1.0, '8': 0.0,
                                 '9': 0.0, '10': -1.0, 'J': -1.0, 'Q': -1.0, 'K': -1.0, 'A': -1.0},
                          'Omega II': {'2': 1.0, '3': 1.0, '4': 2.0, '5': 2.0, '6': 2.0, '7': 1.0,
                                       '8': 0.0, '9': -1.0, '10': -2.0, 'J': -2.0, 'Q': -2.0, 'K': -2.0, 'A': 0.0},
                          'Red 7': {'2': 1.0, '3': 1.0, '4': 1.0, '5': 1.0, '6': 1.0, '7': 1.0,
                                    '8': 0.0, '9': 0.0, '10': -1.0, 'J': -1.0, 'Q': -1.0, 'K': -1.0, 'A': -1.0},
                          'Halves': {'2': 0.5, '3': 1.0, '4': 1.0, '5': 1.5, '6': 1.0, '7': 0.5,
                                     '8': 0.0, '9': -0.5, '10': -1.0, 'J': -1.0, 'Q': -1.0, 'K': -1.0, 'A': -1.0},
                          'Zen Count': {'2': 1.0, '3': 1.0, '4': 2.0, '5': 2.0, '6': 2.0, '7': 1.0,
                                        '8': 0.0, '9': 0.0, '10': -2.0, 'J': -2.0, 'Q': -2.0, 'K': -2.0, 'A': -1.0}}


def gen_deck(deck_num: int):
    """
    Generates a shoe (collection of cards) with 4 identically decks for the user, where suits don't matter
    :param deck_num: the number of decks to generate for the user
    :return: a list of shuffled decks for the user
    """

    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = np.array([i for _ in range(4 * deck_num) for i in ranks], str)
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
    Looks up the available hand sums to find the winner (1) you win, (-1) dealer wins (0) draw between dealer
    :param player_sum: the value of the players hand
    :param dealer_sum: the value of the dealers hand
    :return: an integer from the set of [-1, 0, 1] indicating [loss, draw, win]
    """

    win_dict = {(dealer_sum < player_sum <= 21): 1,
                (player_sum < dealer_sum <= 21): -1,
                (player_sum == dealer_sum): 0,
                (player_sum > 21 and dealer_sum > 21): 0,
                (player_sum > 21 >= dealer_sum): -1,
                (dealer_sum > 21 >= player_sum): 1}

    return win_dict[True]


def bet_check(value: int, funds: int, bet: int):
    """
    Check to see whether to add or subtract value of bet from the funds
    :param value: the value which corresponds to the find_winner function
    :param funds: the amount of funds available specified by the player
    :param bet: the original bet amount specified by the player
    :return: the new funds amount according to win/loss value
    """

    value_assign = {1: bet, -1: -bet, 0: 0}
    return funds + value_assign[value]


def double_func(bet: int, funds: int):
    """
    Double bets and returns either 0 or doubles your initial bet, leverage and available funds
    :param bet: the original bet amount specified by the player
    :param funds: the amount of funds available specified by the player
    :return: returns the new defined bet amount
    """

    doubler = bet * 2
    double_dict = {(doubler <= funds): doubler, (doubler > funds): bet}
    return double_dict[True]


def insurance_func(dealer_list: np.array, funds: int, insurance_bet: int):
    """
    Take out insurance in the event the dealer is showing a high card
    :param dealer_list: a list of card values assigned to the dealer
    :param funds: the amount of funds available specified by the player
    :param insurance_bet: specified insurance bet by user
    :return: returns the insurance bet as specified by the user
    """

    if dealer_list[0] == 'A' and (insurance_bet < funds):
        return insurance_bet


class Game:

    def __init__(self, bet: int, funds: int, side_bet: int = 0, deck_num: int = 4, split: bool = True,
                 insurance: bool = False, double: bool = True, card_counter: str = None):
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
        assert bet > 10, 'Bet value too low, minimum threshold is 10'

        self.deck_num = deck_num
        self.deck = gen_deck(deck_num=self.deck_num)
        self.reshuffle_threshold = 60

        self.bet = bet
        self.funds = funds
        self.split = split
        self.insurance = insurance
        self.double = double
        self.side_bet = side_bet

        self.card_counter = card_counter
        self.cards_played = np.array([])

        self.cs = np.array(['Hi-Lo', 'Hi-Opt I', 'Hi-Opt I', 'KO', 'Omega II', 'Red 7', 'Halves', 'Zen Count'])

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

        # deals a hand of 2 cards to the player and dealer by popping the last unit of the shuffled list
        self.deck, dealers_hand = self.deck[:-2], self.deck[-2:]
        self.deck, players_hand = self.deck[:-2], self.deck[-2:]

        return dealers_hand, players_hand

    def _scaler_(self, rolling_cards: np.array):
        return sum([card_counting_profiles[self.card_counter][card] for card in rolling_cards])

    def blackjack(self, dealers_hand: np.array = None, players_hand: np.array = None):
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

                # if you do not receive a natural 21 then you are asked to hit, stand, double or split
                else:
                    player_ref = ','.join(players_hand)
                    swap_player_ref = '{le},{rg}'.format(le=player_ref[2],
                                                         rg=player_ref[0])
                    hole_card = dealers_hand[0]

                    if player_ref in basic_strategy_profile['A'].keys():
                        action = basic_strategy_profile[hole_card][player_ref]
                    elif swap_player_ref in basic_strategy_profile['A'].keys():
                        action = basic_strategy_profile[hole_card][swap_player_ref]
                    else:
                        action = basic_strategy_profile[hole_card][str(p_sum)]

                    final_dealer_hand = dealer_serve(draw_func=self._hit_,
                                                     dealers_hand=dealers_hand)

                    if action == 'H':
                        players_hand = self._hit_(players_hand)
                        self.funds = self._sequence_(players_hand=players_hand,
                                                     dealer_hand=final_dealer_hand,
                                                     bet=self.bet)

                    elif action == 'S':
                        self.funds = self._sequence_(players_hand=players_hand,
                                                     dealer_hand=final_dealer_hand,
                                                     bet=self.bet)

                    elif action == 'SP' and self.split:
                        players_hand = self._split_(card_list=players_hand)
                        for card in range(0, len(players_hand), 2):
                            new_player_hand = players_hand[card:card + 2]
                            self.blackjack(dealers_hand=final_dealer_hand, players_hand=new_player_hand)

                    elif action == 'D' and self.double:
                        bet_amt = double_func(bet=self.bet, funds=self.funds)
                        players_hand = self._hit_(players_hand)
                        self.funds = self._sequence_(players_hand=players_hand,
                                                     dealer_hand=final_dealer_hand,
                                                     bet=bet_amt)

                    self.cards_played = np.append(self.cards_played, final_dealer_hand)
                    self.cards_played = np.append(self.cards_played, players_hand)

        if self.card_counter in self.cs:
            card_count = self._scaler_(self.cards_played)
            if card_count > 10:
                self.bet += self.bet * 0.1
            elif card_count < -10:
                self.bet -= self.bet * 0.1

        return self.funds


if __name__ == '__main__':
    g = Game(bet=100, funds=10000)
    money = g.blackjack()
    print(money)
