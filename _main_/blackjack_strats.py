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

import blackjack_game as bjg
import matplotlib.pyplot as plt
from multiprocessing import Process, pool
import pandas as pd


class StrategySimulator:

    def __init__(self, num_sim: int, num_hand: int, side_bet: int = 0,
                 deck_num: int = 4, split: bool = True, insurance: bool = False, double: bool = True):

        self.decks = deck_num
        self.num_sims = num_sim
        self.num_hands = num_hand
        self.split = split
        self.insurance = insurance
        self.double = double
        self.side_bet = side_bet

    def _simulation_(self, bet_size: int, fund_size: int):
        master_dict = {}
        for player in range(0, self.num_sims):
            hand_sim = []
            test = bjg.Game(self, bet=bet_size, funds=fund_size, side_bet=self.side_bet, deck_num=self.decks,
                            split=self.split, insurance=self.insurance, double=self.double)
            for i in range(0, self.num_hands):
                pnl = test.blackjack()
                hand_sim.append(pnl)
            master_dict['player_{}'.format(player)] = hand_sim

        return master_dict

