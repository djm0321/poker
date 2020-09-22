import random
import operator
import math
from collections import Counter
from utils import *
from checker import *
from values import *
import gamePlay
from printer import showTable, display

def round(players, blind):
    deck = [i for i in range(52)]
    random.shuffle(deck)
    tableNums = list()
    pot = [0]
    for x in players:
        x.hand = deckToCards(dealHand(deck))
    for x in range(0, 4):
        tableNums = dealer(players, tableNums, deck, x, pot, blind)
    for x in range(0, len(players)):
        print("Player " + str(x + 1) + " now has " + str(players[x].stack))


def dealer(players, table, deck, i, pot, blind):
    "Cleans up round function"
    if (i == 0):
        showTable(players, table)
        gamePlay.betting(players, pot, blind, i)
        display(players, table)
        print(pot)
        return list()
    elif (i == 1):
        table = dealFlop(deck)
        tabled = deckToCards(table)
        showTable(players, tabled)
        gamePlay.betting(players, pot, blind, i)
        display(players, tabled)
        print(pot)
        return table
    elif (i == 2):
        dealR(deck, table)
        tabled = deckToCards(table)
        showTable(players, tabled)
        gamePlay.betting(players, pot, blind, i)
        display(players, tabled)
        print(pot)
        return table
    elif (i == 3):
        dealR(deck, table)
        tabled = deckToCards(table)
        showTable(players, tabled)
        gamePlay.betting(players, pot, blind, i)
        payouts = display(players, tabled)
        print(pot)
        print(payouts)
        for x in payouts:
            players[x].wonPot(int(pot[0]/len(payouts)))
            print("Player " + str(x + 1) + " won $" + str(int(pot[0]/len(payouts))))
        return table

def main(): 
    "Main function for poker"
    # pokerUI.test()
    numPlayers = int(input("Number of Players: "))
    players = list()
    for i in range(0, numPlayers):
        players.append(gamePlay.Player([], [], i))
    gamePlay.giveStartingCash(players)
    blind = 0
    while (input("Play a round? ") != "n"):
        round(players, blind)
        blind+=1
        if (blind == numPlayers):
            blind = 0
        for x in players:
            x.playHand()
            if x.giveStack() == 0:
                players.remove(x)
    
main()