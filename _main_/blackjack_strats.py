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

import blackjack_game as bjg
import matplotlib.pyplot as plt
import multiprocessing as mp


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

        self.game_count = []

    def _simulation_(self, bet_size: int, fund_size: int):
        pool = mp.Pool(mp.cpu_count())

        test = [pool.apply_async(bjg.Game, [bet_size, fund_size, self.side_bet, self.decks, self.split,
                                            self.insurance, self.double]) for _ in range(0, self.num_sims)]
        test_cases = [item.get() for item in test]
        for obj in test_cases:
            ret_list = [pool.apply_async(obj.blackjack) for _ in range(0, self.num_hands)]
            ret = [item.get() for item in ret_list]
            self.game_count.append(bjg.np.array(ret))

        return self.game_count


class Bayesian:

    def __init__(self, mean: int, std: float):
        self.mean = mean
        self.std = std


if __name__ == "__main__":
    import time
    t1 = time.process_time()
    sims = 100
    hands = 200
    bet = 100
    funds = 10000

    g = StrategySimulator(num_sim=sims, num_hand=hands)
    counts = g._simulation_(bet_size=bet, fund_size=funds)
    plt.title('{} simulations over {} hands: Bet size {} _ Funds Available {}'.format(sims, hands, bet, funds))
    plt.plot(counts)
    print(counts)
    # plt.show()
    print(t1-time.process_time())
