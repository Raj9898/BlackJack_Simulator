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
import pandas as pd


class StrategySimulator:

    def __init__(self, num_sim: int, num_hand: int):

        self.num_sims = num_sim
        self.num_hands = num_hand
        self.game_count = []

    def _simulation_(self, bet_size: int, fund_size: int, deck_num: int = 4, card_counter: str = None):

        for _ in range(self.num_sims):
            obj = bjg.Game(bet=bet_size, funds=fund_size, deck_num=deck_num, card_counter=card_counter)
            ret = [obj.blackjack() for _ in range(self.num_hands)]
            self.game_count.append(bjg.np.array(ret))

        return self.game_count


def composite_stat(composite_arr: bjg.np.array):
    avg_arr = (1/len(composite_arr))*bjg.np.sum(composite_arr, axis=0)
    std = bjg.np.std(avg_arr)
    avg_gain = round((avg_arr[-1] - avg_arr[0])/avg_arr[0], 4)

    df = pd.DataFrame(avg_arr).pct_change()
    wins = len(df[df > 0].dropna())
    win_pct = round(wins / len(df), 2)
    return avg_gain, std, win_pct, 1-win_pct


class Bayesian:

    def __init__(self, mean: int, std: float):
        self.mean = mean
        self.std = std


if __name__ == "__main__":
    import time
    t1 = time.process_time()
    sims = 1000
    hands = 150
    bet = 100
    funds = 10000

    g = StrategySimulator(num_sim=sims, num_hand=hands)
    counts = g._simulation_(bet_size=bet, fund_size=funds)
    print(counts)

    # for i in range(len(counts)):
    #     plt.plot(counts[i])
    #
    # plt.title('{} simulations over {} hands: Bet size {} _ Funds Available {}'.format(sims, hands, bet, funds))
    # plt.show()

    # print(composite_stat(counts))

    print(t1-time.process_time())
