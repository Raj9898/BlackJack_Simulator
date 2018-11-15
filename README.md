# BlackJack Simulator & Strategy Profile
This project focuses on simulating game(s) of Blackjack across different Player objects, each with defined strategy profiles over numerous hands to demonstrate the long-term impact on P&L and win/loss percentage, with the intent of developing more effecient betting strategies and optimal play approaches to the game. 

## Basic Rules of Blackjack
These are the general rule of Blackjack as played across most real/virtual casinos throughout the world. <br/>

1. ***Aces may be counted as 1 or 11 points, 2 to 9 according to pip value, and tens and face cards count as ten points.**
2. The value of a hand is the sum of the point values of the individual cards. Except, a "blackjack" is the highest hand, consisting of an ace and any 10-point card, and it outranks all other 21-point hands.
3. After the players have bet, the dealer will give two cards to each player and two cards to himself. One of the dealer cards is dealt face up. The facedown card is called the "hole card."
4. **If the dealer has an ace showing, he will offer a side bet called "insurance." This side wager pays 2 to 1 if the dealer's hole card is any 10-point card. Insurance wagers are optional and may not exceed half the original wager.**
5. If the dealer has a ten or an ace showing (after offering insurance with an ace showing), if the dealer does have a blackjack, then all wagers (except insurance) will lose, unless the player also has a blackjack, which will result in a push. 
6. **Play begins with the player to the dealer's left. The following are the choices available to the player:** 
    - Stand: Player stands pat with his cards.
    - Hit: Player draws another card (and more if he wishes). If this card causes the player's total points to exceed 21 (known as  "breaking" or "busting") then he loses.
    - Double: Player doubles his bet and gets one, and only one, more card.
    - Split: If the player has a pair, or any two 10-point cards, then he may double his bet and separate his cards into two individual hands. The dealer will automatically give each card a second card. Then, the player may hit, stand, or double normally.
7. **After each player has had his turn, the dealer will turn over his hole card. If the dealer has 16 or less, then he will draw another card. A special situation is when the dealer has an ace and any number of cards totaling six points (known as a "soft 17").**
8. If the dealer goes over 21 points, then any player who didn't already bust will win.
9. If the dealer does not bust, then the higher point total between the player and dealer will win.
10. Winning wagers pay even money, except a winning player blackjack pays 3 to 2. 

## Basic Strategy for Implementation
Below is a basic strategy chart for players at casino-tables operating under the most common house rules. The following color codes identify play strategies perceived to be optimal play and are widely considered standard for new players looking to gain a competitive edge at the table. I will be referencing this table heavily when crafting strategies and allocating bet sizes.  <br/>
!['SimpleStrategy'](https://github.com/Raj9898/BlackJack_Simulator/blob/master/_misc_/Blackjack-Basic-Strategy-Chart.png) <br/> 

