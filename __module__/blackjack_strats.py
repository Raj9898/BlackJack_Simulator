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

    def _simulation_(self, bet_size: int, fund_size: int, deck_num: int = 4, deck_pen: float = .2,
                     card_counter: str = None, val_count: str= 'val'):

        choice_dict = {'val': 0, 'cnt': 1, 'bet': 2}

        for _ in range(self.num_sims):
            obj = bjg.Game(bet=bet_size, funds=fund_size, deck_num=deck_num,
                           card_counter=card_counter, deck_pen=deck_pen)
            ret = [obj.blackjack()[choice_dict[val_count]] for _ in range(self.num_hands)]
            self.game_count.append(bjg.np.array(ret))

        return self.game_count


def composite_stats(composite_arr: bjg.np.array):
    avg_arr = bjg.np.mean(composite_arr, axis=0)
    avg_val = round(bjg.np.mean(avg_arr), 2)
    std = round(bjg.np.std(avg_arr), 4)
    avg_gain = round((avg_arr[-1] - avg_arr[0])/avg_arr[0], 4)

    df = pd.DataFrame(avg_arr).pct_change()
    win_pct = round(len(df[df > 0].dropna()) / len(df), 2)

    return avg_arr, avg_val, avg_gain, std, win_pct, round(1-win_pct, 2)


if __name__ == "__main__":
    sims = 100
    hands = 150
    decks = 8
    bet = 100
    funds = 10000
    card_cs = 'Reverse RAPC'

    g = StrategySimulator(num_sim=sims, num_hand=hands)
    money_1 = g._simulation_(bet_size=bet, fund_size=funds, deck_num=decks, val_count='val', card_counter=card_cs)

    h = StrategySimulator(num_sim=sims, num_hand=hands)
    money_2 = h._simulation_(bet_size=bet, fund_size=funds, deck_num=decks, val_count='val')

    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(2, 1, sharex='col')

    for x in money_2:
        axes[0].plot(x)
        axes[0].set_title('Regular Basic Strategy -- {}'.format(composite_stats(money_2)[1]))

    for i in money_1:
        axes[1].plot(i)
        axes[1].set_title('{} wt Kelly -- {}'.format(card_cs, composite_stats(money_1)[1],))

    plt.show()
