## Blackjack Simulator & Strategy Profile
This project proposes a model for sequential betting in repeated games of Blackjack. We establish the rational behavior of gamblers provided standard betting rules and information, and consider a single gambler that receives information as it occurs. For simplicity, we assume the gambler is rationale i.e., the bet size and strategy are determined by existing optimal play charts. 

We first establish the structure of the game, programming the rules and betting policy. This policy determines, given a realization of the current action, how much of the initial funds will be bet, so that the long-term average profit is maximized. When optimizing, we will simulate successive hands across players and sub-strategies. 

Basic strategy chart, simulated over roughly 10000 players over a span of 150 hands. Notice the almost perfectly normalized distribution of returns spanning the sim. With the mean and standard deviation being calculated as follows:

<a href="https://www.codecogs.com/eqnedit.php?latex=$\mu&space;=&space;\sum_{j=0}^{n}\sum_{i=0}^{n}&space;\bar{v}_i_j$" target="_blank"><img src="https://latex.codecogs.com/gif.latex?$\mu&space;=&space;\sum_{j=0}^{n}\sum_{i=0}^{n}&space;\bar{v}_i_j$" title="$\mu = \sum_{j=0}^{n}\sum_{i=0}^{n} \bar{v}_i_j$" /></a> 

<a href="https://www.codecogs.com/eqnedit.php?latex=\sigma&space;=&space;\sqrt{\frac{1}{n}\sum_{i=0}^{n}|x_i-\mu|}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sigma&space;=&space;\sqrt{\frac{1}{n}\sum_{i=0}^{n}|x_i-\mu|}" title="\sigma = \sqrt{\frac{1}{n}\sum_{i=0}^{n}|x_i-\mu|}" /></a>

![alt text](https://github.com/Raj9898/BlackJack_Simulator/blob/master/_misc_/basic_strategy_pnl.png)

Typically, all card counting strategies will tend to oscillate between a range of values but tend to be centered around a mean of 0
![alt text](https://github.com/Raj9898/BlackJack_Simulator/blob/master/_misc_/card_counting_count.png)

General distrubtion of the possible card counting strategies across sucessive hands
![alt text](https://github.com/Raj9898/BlackJack_Simulator/blob/master/_misc_/card_counting_count_dist.png)

Distribution of PnL across basic strategy template and a card counting strategy
![alt text](https://github.com/Raj9898/BlackJack_Simulator/blob/master/_misc_/regular_vs_cc.png)


