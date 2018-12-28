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
import multiprocessing as mp
import pandas as pd


class StrategySimulator:

    def __init__(self, num_sim: int, num_hand: int, side_bet: int = 0, deck_num: int = 4,
                 split: bool = True, insurance: bool = False, double: bool = True):

        self.decks = deck_num
        self.num_sims = num_sim
        self.num_hands = num_hand
        self.split = split
        self.insurance = insurance
        self.double = double
        self.side_bet = side_bet

    def _simulation_(self, bet_size: int, fund_size: int):
        pool = mp.Pool(mp.cpu_count())

        test = [pool.apply_async(bjg.Game, [bet_size, fund_size, self.side_bet, self.decks, self.split,
                                            self.insurance, self.double]) for e in range(0, self.num_sims) ]
        test_cases = [item.get() for item in test]
        for obj in test_cases:
            ret_list = [pool.apply_async(obj.blackjack) for _ in range(0, self.num_hands)]
            ret = [item.get() for item in ret_list]
            print(ret)


if __name__ == "__main__":
    import time
    t1 = time.process_time()
    g = StrategySimulator(num_sim=10000, num_hand=200)
    g._simulation_(bet_size=100, fund_size=100000)
    print(t1-time.process_time())
