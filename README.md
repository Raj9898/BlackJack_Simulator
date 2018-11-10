# BlackJack Simulator & Strategy Profile
The library focuses on simulating game(s) of Blackjack across different Player objects, each with defined strategies played over numerous hands to demonstrate the long-term impact on P&L as well as win/loss %

Script dependencies include Python 3.6 as well as  the random library, numpy and matplotlib'

The entire library runs across three main scripts:
1. blackjack_lib which supplies the necessary infrastructure and back-end functionality for Blackjack_Script_Sim 
2. blackjack_strats stores a system of rules to execute gambling strategies
3. blackjack_game stores the Blackjack Game strucutre to simulate games according to strategies

After a simulation (hand) is played, P&L is calculated and stored to generate plots for visual transperancy. Each plot on the graph represents the overall performance of a Player (strategy) over the course of multiple hands. 

## Basic Strategy Implementation 
Below is a basic chart created for tables using the most common house rules, borrowed from [casinoreviewsquad.com], The following tables illustrates percieved optimal play. 

!['SimpleStrategy'](https://github.com/Raj9898/BlackJack_Simulator/blob/master/_strats_/Blackjack-Basic-Strategy-Chart.png) 
