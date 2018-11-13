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

import numpy
import pandas as pd
import blackjack_lib as bjk


class Game:
    """
    Initializes the game with predefined arguments regarding game structure
        bet:        determines the size of initial and subsequent bets (type integer)
        funds:      determines starting funds for the game (type integer)
        side_bet:   determines the size of side_bet in the event of insurance (type integer)
        split:      indicates the player's preference to split if available (type bool)
        insurance:  indicates the player's preference to take out insurance if available (type bool)
        double:     indicates the player's preference to double if available (type bool)
        leverage:   indicates the player's preference to use leverage (type bool)
    """

    def __init__(self, bet: int, funds: int, side_bet: int=0, deck_num: int=4, split: bool =True,
                 insurance: bool =False, double: bool =True, leverage: bool =False):
        assert bet < funds, "The value of your bet exceeds your total funds"

        self.deck = bjk.gen_deck(deck_num=deck_num)
        self.reshuffle = len(self.deck)/4

        self.bet = bet
        self.funds = funds
        self.split = split
        self.insurance = insurance
        self.double = double
        self.side_bet = side_bet
        self.lev = leverage

        numpy.random.shuffle(self.deck)

    def hit(self, some_list: list):
        """
        Hit functionality for another card to be drawn for the user
        :param some_list: referencing the player/dealer hands
        :return: a new list with an additional card added
        """
        new_card = self.deck.pop()
        some_list.append(new_card)
        return some_list

    def split(self, players_hand: list):
        splitting = bjk.split(players_hand)
        return splitting

    def double(self, bet: int, funds: int):
        bet_amt = bjk.double(bet, funds)
        return bet_amt

    def stand(self):
        return 0

    def blackjack(self):
        """
        simulates a game of blackjack as per specification imputed by user
        return: available funds after successful completion of hand
        """

        dealers_hand = []
        players_hand = []

        if self.funds > 0:

            # deals a hand of 2 cards to the player and dealer by popping the last unit of the shuffled list
            for x in range(0, 2):
                dealer_card = self.deck.pop()
                dealers_hand.append(dealer_card)

                player_card = self.deck.pop()
                players_hand.append(player_card)

            # insurance mechanic if the dealer presents an Ace
            if self.insurance:
                self.side_bet = bjk.insurance(dealers_hand, self.funds, self.side_bet)
            else:
                self.side_bet = 0

            # returns the sum of player's and the dealer's respective hand value
            d_sum = bjk.sum_hand(dealers_hand)
            p_sum = bjk.sum_hand(players_hand)

            # checks to see if dealer has a natural 21 on the first draw/deal
            if d_sum == 21 and p_sum < 21:
                self.funds -= self.bet
                self.funds += (self.side_bet * 2)

            # checks to see if their is a tie of natural 21 signaling a push
            elif d_sum == 21 & p_sum == 21:
                pass

            else:
                # if the dealer does not hit a natural 21 you lose your side bet (insurance)
                self.funds -= self.side_bet

                # if you receive a natural 21 you receive a 3:2 payout and dealer loses
                if p_sum == 21:
                    self.funds += ((self.bet / 2) * 3)

                # if you do not receive a natural 21 then you are asked to hit, stand, double or split
                else:
                    strategy_df = pd.read_csv('blackjack_basic_strategy.csv')
                    player_ref = ','.join(players_hand)
                    hole_card = dealers_hand.pop()

                    # strategy_df['Players Hand']




                    # # if you do not want to split this sequence is executed
                    # if not self.split:
                    #
                    #     # asks you if you would like to double your bet
                    #     new_bet = bjk.double(self.bet, self.funds)
                    #
                    #     # if you do want to double, this sequence is executed
                    #     if self.double == True and p_sum == self.double_stop:
                    #         # the bet is now doubled accordingly
                    #         self.bet = new_bet
                    #
                    #         # your are now dealt one additional card
                    #         news = self.hit()
                    #         new_score = (bjk.sum_hand(bjk.int_card(news)))
                    #
                    #         # makes the dealer draw cards until he reaches a sum >= 17
                    #         while d_sum < 17:
                    #             d_sum = bjk.d_sev(self.draw())
                    #             if d_sum > 16:
                    #                 break
                    #
                    #         # checks to find the winner given the available hands
                    #         winner = bjk.find_winner(new_score, d_sum)
                    #
                    #         self.funds = bjk.bet_check(winner, self.funds, self.bet)
                    #         self.bet = new_bet / 2
                    #
                    #     # if you do not want to double this sequence is executed
                    #     elif self.double == False or self.double == True:
                    #
                    #         # if you elect to hit this sequence is executed
                    #         while p_sum < self.hit_stop:
                    #             news = self.hit()
                    #             new_score = (bjk.sum_hand(bjk.int_card(news)))
                    #             p_sum = new_score
                    #
                    #         # makes the dealer draw cards until he reaches a sum >= 17
                    #         while d_sum < 17:
                    #             d_sum = bjk.d_sev(self.draw())
                    #             if d_sum > 16:
                    #                 break
                    #
                    #         # checks to find the winner of the available hands
                    #         winner = bjk.find_winner(p_sum, d_sum)
                    #         self.funds = bjk.bet_check(winner, self.funds, self.bet)
                    #
                    #
                    # elif self.split == True and splitting != 0:
                    #
                    #     self.funds -= side_bet
                    #
                    #     # in the event you split you play each hand independently
                    #     for x in range(0, len(splitting)):
                    #
                    #         # iterates over each hand and executes each hand accordingly
                    #         split_hand = splitting[x]
                    #
                    #         # asks you if you would like to double your bet and receive one and only one additional card
                    #         new_bet = bjk.double(self.bet, self.funds, self.lev)
                    #
                    #         # if you do want to double, this sequence is executed
                    #         if self.double == True and p_sum == self.double_stop:
                    #             # the bet is now doubled accordingly
                    #             self.bet = new_bet
                    #
                    #             # your are now dealt one additional card
                    #             news = self.split_hit(split_hand)
                    #             new_score = (bjk.sum_hand(bjk.int_card(news)))
                    #
                    #             # makes the dealer draw cards until he reaches a sum >= 17
                    #             while d_sum < 17:
                    #                 d_sum = bjk.d_sev(self.draw())
                    #                 if d_sum > 16:
                    #                     break
                    #
                    #             # checks to find the winner given the available hands
                    #             winner = bjk.find_winner(new_score, d_sum)
                    #
                    #             self.funds = bjk.bet_check(winner, self.funds, self.bet)
                    #             self.bet = new_bet / 2
                    #
                    #         # if you do not want to double this sequence is executed
                    #         elif self.double == False or self.double == True:
                    #
                    #             # if you elect to hit this sequence is executed
                    #             while p_sum < self.hit_stop:
                    #                 news = self.split_hit(split_hand)
                    #                 new_score = (bjk.sum_hand(bjk.int_card(news)))
                    #                 p_sum = new_score
                    #
                    #             # makes the dealer draw cards until he reaches a sum >= 17
                    #             while d_sum < 17:
                    #                 d_sum = bjk.d_sev(self.draw())
                    #                 if d_sum > 16:
                    #                     break
                    #
                    #             # checks to find the winner of the available hands
                    #             winner = bjk.find_winner(p_sum, d_sum)
                    #             self.funds = bjk.bet_check(winner, self.funds, self.bet)

        return self.funds


if __name__ == "__main__":
    
    test = Game(bet=100, funds=10000)
    test.blackjack()

    


