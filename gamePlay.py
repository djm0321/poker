class Player():
    def __init__(self, hand, stack, num):
        self.hand = hand
        self.stack = stack
        self.play = True
        self.betVal = 0
        self.player = num
    
    def playHand(self):
        self.play = True
    
    def fold(self):
        self.play = False

    def playing(self):
        return self.play
    
    def giveStartingCash(self):
        self.stack(1500)
    
    def bet(self, amnt, pot):
        if (self.stack - amnt >= 0):
            self.stack -= amnt
            pot[0] += amnt
            self.betVal = amnt
        else:
            print("Cannot bet that amount. Going all in and creating a side pot.")
            pot[0] += self.stack
            self.stack = 0
    
    def giveStack(self):
        return self.stack
    
    def wonPot(self, pot):
        self.stack += pot
    
    def getBet(self):
        return self.betVal

    def startBet(self):
        self.betVal = 0

class Pot():
    def __init__(self, size, players):
        self.size = size
        self.players = players

    def added(self, bet):
        self.size += bet


def fold (player):
    player.play = False

def giveStartingCash(players):
    for x in range(0, len(players)):
        players[x].stack = 1500

def bet(player, amnt, pot):
    player.stack = player.stack - amnt
    pot[0] = pot[0] + amnt

def winPot(player, pot):
    player.stack += pot
 
def blinds(players, blind, pot):
    players[blind].bet(25, pot)
    print("player " + str(blind + 1) + " was small blind.")
    players[blind + 1].bet(50, pot)
    print("player " + str(blind + 2) + " was big blind.")
    return 50

def resetBets(players):
    for x in players:
        x.startBet()

def betting(players, pot, blind, round):
    print(round)
    print("Start the betting!")
    resetBets(players)
    highBet = 0
    raiser = blind
    newHigh = False
    p = blind
    if(round == 0):
        highBet = blinds(players, blind, pot)
        p = blind + 2
        raiser = blind + 1
    s = False
    while (raiser != p) or not s:
        if not s:
            s = True
        if players[p].playing():
            b = input("Player " + str(p + 1) + " bet: ")
            if not b:
                if highBet != 0:
                    players[p].fold()
                else:
                    b = 0
            else:
                if b == "c":
                    b = highBet
                elif b.isdigit():
                    if int(b) <= highBet:
                        b = highBet
                    else:
                        highBet = int(b)
                        b = int(b)
                        newHigh = True
                players[p].bet(b - players[p].getBet(), pot)
        if newHigh:
            raiser = p
            newHigh = False
        p += 1
        if p == len(players):
            p = 0