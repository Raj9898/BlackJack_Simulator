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
    def __init__(self, bet, funds, rand, hit_stop=15, side_bet=0, double_stop=0, split=False, insurance=False,
                 double=False,
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
    def __init__(self, bet, funds, rand, hit_stop=15, side_bet=0, double_stop=11, split=False, insurance=False,
                 double=True,
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
                self.bet = (standard_bet / 2)
                win += 1

        plt.subplot(132)
        plt.title('Leverage Betting')
        plt.plot(PnL, 'g')

        win_loss = win / (win + loss)
        return win_loss, PnL


# synthetic dealer/player strategy
class Player3(Game):
    # initializes the functionality for Player 3
    def __init__(self, bet, funds, rand, hit_stop=16, side_bet=0, double_stop=13, split=True, insurance=False,
                 double=True,
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
