"""
Blackjack Game
@Rajesh
12/11/2017
"""

'''
IMPORT MODULES
'''
import random as r
import numpy as n
import matplotlib.pyplot as plt
import Blackjack_Lib_Sim as bjk

'''
MAIN GAME SEQUENCE
# defines the game structure and outline for blackjack with basic rules
# 2-10 are face value,J, Q, K are 10 equivalents and A is 11 for natural 21
# player has the option to hit, stand, double or split
# hit draws another card and appends to players existing hand
# stand lets the player stick with his hand and does not draw
# double doubles the players bet and then draws them one and only one card
# split, splits the players hand and allows them to play each hand seperately
'''


class Game:
    # initializes the game with deck, player(s), dealer's hand, bet and initial funds
    def __init__(self, bet, funds, hit_stop=15, side_bet=0, double_stop=0, split=False, insurance=False, double=False,
                 lev=False):
        if lev == False:
            assert bet < funds, "The value of your bet exceeds your total funds"
        else:
            pass
        assert type(split) == bool and type(insurance) == bool and type(double) == bool
        assert type(side_bet) == int or type(side_bet) == float
        assert type(hit_stop) == int

        self.deck = bjk.gen_deck()
        self.bet = bet
        self.funds = funds
        self.dealer = []
        self.hand = []
        self.split = split
        self.insurance = insurance
        self.double = double
        self.side_bet = side_bet
        self.hit_stop = hit_stop
        self.double_stop = double_stop
        self.lev = lev

        self.win = 0
        self.loss = 0

    # defines the blackjack sequence or game structure
    def blackjack(self, random = True):
        assert type(random) == bool
        
        if self.funds > 0:

            # shuffles the deck for the game using random library
            if random == True:
                r.shuffle(self.deck)
            elif random == False:
                n.random.shuffle(self.deck)
                
            player_hand = self.deal_cards()

            for i in player_hand:
                self.deck.append(i)
            for y in self.dealer:
                self.deck.append(y)

            # iterates over the hand to extrapolate the important numeric/value
            p_list = bjk.int_card(player_hand)
            d_list = bjk.int_card(self.dealer)

            # allows you to take out insurance if the dealer is showing an Ace
            if self.insurance == True:
                side_bet = bjk.insurance(d_list, self.funds, self.side_bet)
            else:
                side_bet = 0

            # returns the sum of participants and the dealers hand to be compared
            d_sum = bjk.sum_hand(d_list)
            p_sum = bjk.sum_hand(p_list)

            # checks to see if dealer has a natural 21 on the first draw/deal
            if d_sum == 21 and p_sum < 21:
                self.funds -= self.bet
                # while you may lose your initial bet you receive your side bet in compensation
                self.funds += (self.side_bet * 2)


            # checks to see if their is a tie of natural 21 signaling a push
            elif d_sum == 21 and p_sum == 21 or d_sum > 21 and p_sum > 21:
                pass

            elif d_sum > 21 and p_sum < 21:
                self.funds += self.bet
                self.funds += (self.side_bet * 2)


            # if above mentioned cases don't pass you are now allowed to either hit, stand, double or split
            else:
                # if the dealer does not hit a natural 21 you lose your side bet (insurance)
                self.funds -= self.side_bet

                # if you receive a natural 21 you receive a 3:2 payout and dealer loses
                if p_sum == 21:
                    self.funds += ((self.bet / 2) * 3)

                # if you receive a double Ace
                elif p_sum > 21:
                    self.funds -= self.bet

                # if you do not receive a natural 21 then you are asked to hit, stand, double or split
                else:
                    # split functionality that checks the values in player hand are identical
                    splitting = bjk.split(p_list, player_hand)

                    # if you do not want to split this sequence is executed   
                    if self.split == False:

                        # asks you if you would like to double your bet and receive one and only one additional card
                        new_bet = bjk.double(self.bet, self.funds, self.lev)

                        # if you do want to double, this sequence is executed
                        if self.double == True and p_sum == self.double_stop:
                            # the bet is now doubled accordingly
                            self.bet = new_bet

                            # your are now dealt one additional card
                            news = self.hit()
                            new_score = (bjk.sum_hand(bjk.int_card(news)))

                            # makes the dealer draw cards until he reaches a sum >= 17
                            while d_sum < 17:
                                d_sum = bjk.d_sev(self.draw())
                                if d_sum > 16:
                                    break

                            # checks to find the winner given the available hands
                            winner = bjk.find_winner(new_score, d_sum)

                            self.funds = bjk.bet_check(winner, self.funds, self.bet)
                            self.bet = new_bet / 2

                        # if you do not want to double this sequence is executed
                        elif self.double == False or self.double == True:

                            # if you elect to hit this sequence is executed
                            while p_sum < self.hit_stop:
                                news = self.hit()
                                new_score = (bjk.sum_hand(bjk.int_card(news)))
                                p_sum = new_score

                            # makes the dealer draw cards until he reaches a sum >= 17
                            while d_sum < 17:
                                d_sum = bjk.d_sev(self.draw())
                                if d_sum > 16:
                                    break

                            # checks to find the winner of the available hands
                            winner = bjk.find_winner(p_sum, d_sum)
                            self.funds = bjk.bet_check(winner, self.funds, self.bet)


                    elif self.split == True and splitting != 0:

                        self.funds -= side_bet

                        # in the event you split you play each hand independently 
                        for x in range(0, len(splitting)):

                            # iterates over each hand and executes each hand accordingly
                            split_hand = splitting[x]

                            # asks you if you would like to double your bet and receive one and only one additional card
                            new_bet = bjk.double(self.bet, self.funds, self.lev)

                            # if you do want to double, this sequence is executed
                            if self.double == True and p_sum == self.double_stop:
                                # the bet is now doubled accordingly
                                self.bet = new_bet

                                # your are now dealt one additional card
                                news = self.split_hit(split_hand)
                                new_score = (bjk.sum_hand(bjk.int_card(news)))

                                # makes the dealer draw cards until he reaches a sum >= 17
                                while d_sum < 17:
                                    d_sum = bjk.d_sev(self.draw())
                                    if d_sum > 16:
                                        break

                                # checks to find the winner given the available hands
                                winner = bjk.find_winner(new_score, d_sum)

                                self.funds = bjk.bet_check(winner, self.funds, self.bet)
                                self.bet = new_bet / 2

                            # if you do not want to double this sequence is executed
                            elif self.double == False or self.double == True:

                                # if you elect to hit this sequence is executed
                                while p_sum < self.hit_stop:
                                    news = self.split_hit(split_hand)
                                    new_score = (bjk.sum_hand(bjk.int_card(news)))
                                    p_sum = new_score

                                # makes the dealer draw cards until he reaches a sum >= 17
                                while d_sum < 17:
                                    d_sum = bjk.d_sev(self.draw())
                                    if d_sum > 16:
                                        break

                                # checks to find the winner of the available hands
                                winner = bjk.find_winner(p_sum, d_sum)
                                self.funds = bjk.bet_check(winner, self.funds, self.bet)

        # empties both the player's and dealer's hand to then play again
        self.dealer = []
        self.hand = []

        return self.funds

    # deals a hand of 2 cards to the player and dealer by pop-ing the last unit of the shuffled list
    def deal_cards(self):

        for x in range(0, 2):
            # dealer is dealt first 2 cards
            deals = self.deck.pop()
            self.dealer.append(deals)

            # player(s) are now dealt 2 cards
            deal = self.deck.pop()
            self.hand.append(deal)

        return self.hand

    # hit for another card to be drawn by the user
    def hit(self):
        # new card is added to your hand
        new_card = self.deck.pop()
        self.hand.append(new_card)
        return self.hand

    # hit within the split function
    def split_hit(self, some_list):
        # new card is added to your hand
        new_card = self.deck.pop()
        some_list.append(new_card)
        return some_list

    # executes the continued draw function of the dealer
    def draw(self):
        # the dealer draws a card
        new_card = self.deck.pop()
        self.dealer.append(new_card)
        return self.dealer


'''
PLAYER OBJECTS / STRATEGIES
 # in the Player object there are 10 inputs, 7 of which are given and three must be provided
    # input: bet = how much you would like to bet
    #        fund = your total starting fundss
    #        rand = the type of distirbution you woudl like to use
                    # True = standard random, False = numpy.random
    #       hit_stop = sets the point at which the player will stop hitting, default = 15
    #       side_bet = establishes a side bet in the event insurance is True, default = 0
    #       double_stop = sets the point at which the double will take effect if allowed to, default = 0
    #       split = allows the player to split in the event,default = False
    #       insurance = allows the player to take out insurance in the event, default = False
    #       double = allows the player to engage in doubling his bet, default = False
    #       lev = allows for the player to use leverage in his bet, default = False
    
'''
plt.figure(1, figsize=(15, 5))

# simple strategy or control study
class Player1(Game):
    # returns the name of the participant and stores a variable self.hand
    def __init__(self, bet, funds, rand, hit_stop=15, side_bet=0, double_stop=0, split=False, insurance=False, double=False,
                 lev=False):
        Game.__init__(self, bet, funds, hit_stop, side_bet, double_stop, split, insurance, double, lev)
        self.funds = funds
        self.rand = rand

    def strategy(self):
        money = Game.blackjack(self, self.rand)
        return money

    def simulations(self, num_simulation):
        PnL = [self.funds]
        win = 0
        loss = 0

        for i in range(0, num_simulation):
            num = self.strategy()
            PnL.append(num)

            if PnL[i] < PnL[i - 1]:
                loss += 1
            elif PnL[i] > PnL[i - 1]:
                win += 1
        
        plt.subplot(131)
        plt.title('Control Study')
        plt.plot(PnL, 'r')

        win_loss = win / (win + loss)
        return win_loss, PnL


# advanced leverage speculator strategy
class Player2(Game):
    # initializes the functionality for Player 2
    def __init__(self, bet, funds, rand,  hit_stop=15, side_bet=0, double_stop=11, split=False, insurance=False, double=True,
                 lev=True):
        Game.__init__(self, bet, funds, hit_stop, side_bet, double_stop, split, insurance, double, lev)
        self.bet = bet
        self.funds = funds
        self.rand = rand
    
    # executes the blackjack game
    def strategy(self):
        money = Game.blackjack(self, self.rand)
        return money
    
    # defines the strategy functionality that impact player choice
    def simulations(self, num_simulation, standard_bet):
        PnL = [self.funds]
        win = 0
        loss = 0
        
        for i in range(0, num_simulation):
            num = self.strategy()
            PnL.append(num)

            if PnL[i] < PnL[i - 1]:
                self.bet += (self.bet * .25)
                loss += 1
            elif PnL[i] > PnL[i - 1]:
                self.bet = (standard_bet/2)
                win += 1
        
        plt.subplot(132)
        plt.title('Leverage Betting')
        plt.plot(PnL, 'g')

        win_loss = win / (win + loss)
        return win_loss, PnL


# synthetic dealer/player strategy
class Player3(Game):
    # initializes the functionality for Player 3
    def __init__(self, bet, funds, rand, hit_stop=16, side_bet=0, double_stop=13, split=True, insurance=False, double=True,
                 lev=False):
        Game.__init__(self, bet, funds, hit_stop, side_bet, double_stop, split, insurance, double, lev)
        self.bet = bet
        self.funds = funds
        self.rand = rand
    
    # executes the blackjack game
    def strategy(self):
        money = Game.blackjack(self, self.rand)
        return money
    
    # defines the strategy functionality that impact player choice
    def simulations(self, num_simulation):
        PnL = [self.funds]
        win = 0
        loss = 0

        for i in range(0, num_simulation):
            num = self.strategy()
            PnL.append(num)

            if PnL[i] < PnL[i - 1]:
                loss += 1
            elif PnL[i] > PnL[i - 1]:
                win += 1
        
        plt.subplot(133)
        plt.title('Synthethic Betting')
        plt.plot(PnL, 'b')

        win_loss = win / (win + loss)
        return win_loss, PnL


'''
PROGRAM RUNNING SCRIPT
# executes the program and allows for object manipulation 
# initializes the game object
'''
if __name__ == "__main__":
    
    num_hand = 100
    num_players = 100
    initial_bet = 100
    total_fund = 1000
    
    
    for i in range(0, num_players):
        p1 = Player1(initial_bet, total_fund, False)
        p2 = Player2(initial_bet, total_fund, False)
        p3 = Player3(initial_bet, total_fund, False)
        
        p1.simulations(num_hand)
        p2.simulations(num_hand, initial_bet)
        p3.simulations(num_hand)
        

