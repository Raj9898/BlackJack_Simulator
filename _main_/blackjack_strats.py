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
import pandas as pd

card_counting_strats = ['Hi-Lo', 'Hi-Opt I', 'Hi-Opt II', 'KO', 'Omega II', 'Red 7', 'Halves', 'Zen Count']

count_strategy_df = pd.read_csv('card_count_strategy.csv')
count_strategy_df = count_strategy_df.set_index('Card Counting Strategies')