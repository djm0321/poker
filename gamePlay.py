class Player():
    def __init__(self, hand, stack):
        self.hand = hand
        self.stack = stack
        self.play = True

def fold (players, num):
    players[num].play = False

def giveStartingCash(players):
    for x in range(0, len(players)):
        players[x].stack = 1500

def bet(player, amnt, pot):
    player.stack -= amnt
    pot += amnt
    return pot

def winPot(player, pot):
    player.stack += pot
 
def blinds(players):
    print("bleh")