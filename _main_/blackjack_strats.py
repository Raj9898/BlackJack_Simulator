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
import matplotlib.pyplot as plt


class StrategySimulator:

    def __init__(self, num_sim: int, num_hand: int):

        self.num_sims = num_sim
        self.num_hands = num_hand
        self.game_count = []

    def _simulation_(self, bet_size: int, fund_size: int, deck_num: int = 4,
                     card_counter: str = None, val_count: str= 'val'):

        choice_dict = {'val': 0, 'cnt': 1, 'bet': 2}

        for _ in range(self.num_sims):
            obj = bjg.Game(bet=bet_size, funds=fund_size, deck_num=deck_num, card_counter=card_counter)
            ret = [obj.blackjack()[choice_dict[val_count]] for _ in range(self.num_hands)]
            self.game_count.append(bjg.np.array(ret))

        return self.game_count


def composite_stat(composite_arr: bjg.np.array):
    avg_arr = bjg.np.mean(composite_arr, axis=0)
    avg_val = bjg.np.mean(avg_arr)
    std = bjg.np.std(avg_arr)
    avg_gain = round((avg_arr[-1] - avg_arr[0])/avg_arr[0], 4)

    df = pd.DataFrame(avg_arr).pct_change()
    wins = len(df[df > 0].dropna())
    win_pct = round(wins / len(df), 2)
    return avg_val, avg_gain, std, win_pct, round(1-win_pct, 2)


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
    counts = g._simulation_(bet_size=bet, fund_size=funds, card_counter='Omega II', val_count='val')

    for i in range(len(counts)):
        plt.plot(counts[i])

    avg_mean, avg_g, std_v, win_, loss_pct = composite_stat(counts)
    score = ((avg_mean-funds)/std_v) * win_
    plt.title('{} Valued Option'.format(score))
    plt.figtext(0.15, 0.85, r'$\mu$: {}  $\sigma$: {}'
                            r' Wins: {} Losses:{}'.format(round(avg_mean, 2),
                                                          round(std_v, 4),
                                                          win_,
                                                          loss_pct)
                )
    plt.show()

    print('Time Process running', t1-time.process_time())
