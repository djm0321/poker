import random
import operator
import math
from collections import Counter
from utils import *
from checker import *
from values import *
import findProbs
import gamePlay
# import pokerUI

def printer(cards):
    for x in cards:
        print(faceCardGetter(x.number + 1) + " of " + suitGetter(x.suit))
        # pokerUI.give(faceCardGetter(x.number + 1) + " of " + suitGetter(x.suit))
    print("")

def suitGetter(num):
    if(num == 0):
        return "hearts"
    elif(num == 1):
        return "diamonds"
    elif(num == 2):
        return "spades"
    elif(num == 3):
        return "clubs"
    else:
        return "enter an actual suit u fkin idiot"

def faceCardGetter(num):
    "to say king queen jack ace"
    if num < 11:
        return str(num)
    elif num == 11:
        return "jack"
    elif num == 12:
        return "queen"
    elif num == 13:
        return "king"
    elif num == 14:
        return "ace"


def display(players, table):
    "Displays hands and table to console"
    values = list()
    fullHands = [None] * len(players)
    for x in range(0, len(players)):
        printer(players[x].hand)
        fullHands[x] = players[x].hand + table
        values.append(makeBestHand(fullHands[x]))
    printer(table)
    winner = list()
    printPowers(values)
    topHand(values, winner)
    w = winner[0]
    wins = 0
    wnum = 0
    winners = 0
    for x in values:
        if x.power == w.power and sameHands(x.specs, w.specs):
            wnum = wins
            winners += 1
        wins += 1
    if (winners == 1):
        print("hand " + str(wnum + 1) + " wins")
    # fhand1 = hand1 + table
    # fhand2 = hand2 + table
    # v1 = makeBestHand(fhand1)
    # v2 = makeBestHand(fhand2)
    # compareHands(v1, v2)
    input()

def round(players):
    deck = [i for i in range(52)]
    random.shuffle(deck)
    table = list()
    tableNums = list()
    for x in range(0, len(players)):
        players[x].hand = deckToCards(dealHand(deck))
    for x in range(0, 4):
        tableNums = dealer(players, tableNums, deck, x)

def dealer(players, table, deck, i):
    "Cleans up round function"
    if (i == 0):
        display(players, table)
        return list()
    elif (i == 1):
        table = dealFlop(deck)
        tabled = deckToCards(table)
        display(players, tabled)
        return table
    elif (i > 1):
        dealR(deck, table)
        tabled = deckToCards(table)
        display(players, tabled)
        return table
    # elif (i == 3):
    #     dealR(deck, table)
    #     tabled = deckToCards(table)
    #     display(players, tabled)
    #     return table
    else:
        print("WTF is going on?")

def main(): 
    "Main function for poker"
    # pokerUI.test()
    numPlayers = int(input())
    players = list()
    for i in range(0, numPlayers):
        players.append(gamePlay.Player([], []))
    gamePlay.giveStartingCash(players)
    round(players)
    
    
main()