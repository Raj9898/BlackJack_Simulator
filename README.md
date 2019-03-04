## Blackjack Simulator & Strategy Profile
This project proposes a model for sequential betting in repeated games of Blackjack. We establish the rational behavior of gamblers provided standard betting rules and information, and consider a single gambler that receives information as it occurs. For simplicity, we assume the gambler is rationale i.e., the bet size and strategy are determined by existing optimal play charts. 

We first establish the structure of the game, programming the rules and betting policy. This policy determines, given a realization of the current action, how much of the initial funds will be bet, so that the long-term average profit is maximized. When optimizing, we will simulate successive hands across players and sub-strategies. 

Basic strategy chart, simulated over roughly 10000 players over a span of 150 hands. Notice the almost perfectly normalized distribution of returns spanning the sim. With the mean and standard deviation being calculated as follows:

![alt text](https://github.com/Raj9898/BlackJack_Simulator/blob/master/__misc__/basic_strategy_pnl.png)

Card counting is a technique of strategically assigning values to played cards in order to determine whether the next hand is likely to give a probable edge to the player or to the dealer. The most common variations of these counting techniques in blackjack are based on statistical evidence that high cards (especially aces and 10s) benefit the player more than the dealer, while the low cards, (3s, 4s, 5s and 6s) help the dealer while hurting the player. Typically, all card counting strategies will tend to oscillate between a range of values but tend to be centered around a mean of 0.
![alt text](https://github.com/Raj9898/BlackJack_Simulator/blob/master/__misc__/card_counting_count.png)

The ideal system is a system that is usable by the player and offers the highest average dollar return per period of time when dealt at a fixed rate. With this in mind, systems aim to achieve a balance of efficiency in three categories: 
- **Betting correlation (BC)** when the sum of all the permutations of the undealt cards offer a positive expectation to a player using optimal playing strategy, there is a positive expectation to a player placing a bet. A system's BC gauges how effective a system is at informing the user of this situation.
- **Playing efficiency (PE)** a portion of the expected profit comes from modifying playing strategy based on the known altered composition of cards. For this reason, a system's PE gauges how effectively it informs the player to modify strategy according to the actual composition of undealt cards. A system's PE is important when the effect of PE has a large impact on total gain, as in single- and double-deck games.
- **Insurance correlation (IC)** a portion of expected gain from counting cards comes from taking the insurance bet, which becomes profitable at high counts. An increase in IC will offer additional value to a card counting system.

General distrubtion of the possible card counting strategies across sucessive hands
![alt text](https://github.com/Raj9898/BlackJack_Simulator/blob/master/__misc__/card_counting_count_dist.png)

When comparing the distribution of PnL across basic strategy templates and a card counting strategy, it is apparent that player's receive a slight probabilistic edge which can be exploited through sequential betting adjustments in accordance to the value of the count. Utilziing a modified Kelly criterion to adjust bets, the PnL follows:  
![alt text](https://github.com/Raj9898/BlackJack_Simulator/blob/master/__misc__/regular_vs_cc.png)


