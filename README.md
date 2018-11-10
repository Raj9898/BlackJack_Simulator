# BlackJack Simulator & Strategy Profile
The library focuses on simulating game(s) of Blackjack across different Player objects, each with defined strategies played over numerous hands to demonstrate the long-term impact on P&L as well as win/loss %

The entire library runs across three main scripts:
1. blackjack_lib which supplies the necessary infrastructure and back-end functionality for Blackjack_Script_Sim 
2. blackjack_strats stores a system of rules to execute gambling strategies
3. blackjack_game stores the Blackjack Game structure to simulate games according to strategies

After a simulation (hand) is played, P&L is calculated and stored to generate plots for visual transparency. Each plot on the graph represents the overall performance of a Player (strategy) over the course of multiple hands. 

## Basic Rules of Blackjack
These are the general rule of Blackjack as played across most real/virtual casinos throughout the world. <br/>

1. Blackjack may be played with one to eight decks of 52-card decks.
2. ***Aces may be counted as 1 or 11 points, 2 to 9 according to pip value, and tens and face cards count as ten points.**
3. The value of a hand is the sum of the point values of the individual cards. Except, a "blackjack" is the highest hand, consisting of an ace and any 10-point card, and it outranks all other 21-point hands.
4. After the players have bet, the dealer will give two cards to each player and two cards to himself. One of the dealer cards is dealt face up. The facedown card is called the "hole card."
5. **If the dealer has an ace showing, he will offer a side bet called "insurance." This side wager pays 2 to 1 if the dealer's hole card is any 10-point card. Insurance wagers are optional and may not exceed half the original wager.**
6. If the dealer has a ten or an ace showing (after offering insurance with an ace showing), then he will peek at his facedown card to see if he has a blackjack. If he does, then he will turn it over immediately.
7. If the dealer does have a blackjack, then all wagers (except insurance) will lose, unless the player also has a blackjack, which will result in a push. The dealer will resolve insurance wagers at this time.
8. **Play begins with the player to the dealer's left. The following are the choices available to the player:** 
    - Stand: Player stands pat with his cards.
    - Hit: Player draws another card (and more if he wishes). If this card causes the player's total points to exceed 21 (known as  "breaking" or "busting") then he loses.
    - Double: Player doubles his bet and gets one, and only one, more card.
    - Split: If the player has a pair, or any two 10-point cards, then he may double his bet and separate his cards into two individual hands. The dealer will automatically give each card a second card. Then, the player may hit, stand, or double normally. However, when splitting aces, each ace gets only one card. Sometimes doubling after splitting is not allowed. If the player gets a ten and ace after splitting, then it counts as 21 points, not a blackjack. Usually the player may keep re-splitting up to a total of four hands. Sometimes re-splitting aces is not allowed.
9. **After each player has had his turn, the dealer will turn over his hole card. If the dealer has 16 or less, then he will draw another card. A special situation is when the dealer has an ace and any number of cards totaling six points (known as a "soft 17"). At some tables, the dealer will also hit a soft 17.**
10. If the dealer goes over 21 points, then any player who didn't already bust will win.
11. If the dealer does not bust, then the higher point total between the player and dealer will win.
12. Winning wagers pay even money, except a winning player blackjack usually pays 3 to 2. 

## Basic Strategy for Implementation
Below is a basic strategy chart for players at casino-tables operating under the most common house rules. The following color codes identify play strategies perceived to be optimal play and are widely considered standard for new players looking to gain a competitive edge at the table. I will be referencing this table heavily when crafting strategies and allocating bet sizes.  <br/>
!['SimpleStrategy'](https://github.com/Raj9898/BlackJack_Simulator/blob/master/_strats_/Blackjack-Basic-Strategy-Chart.png) <br/> 

