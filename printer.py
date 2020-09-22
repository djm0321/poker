from utils import *

def printer(cards):
    for x in cards:
        print(faceCardGetter(x.number + 1) + " of " + suitGetter(x.suit))
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

def showTable(players, table):
    "display got used as a way to find winners so I need to separate those"
    for x in range(0, len(players)):
        if players[x].playing():
            printer(players[x].hand)
        else:
            print("Player " + str(x + 1) + " Has Folded")
            print()
    printer(table)

def display(players, table):
    "Displays hands and table to console"
    values = list()
    fullHands = [None] * len(players)
    for x in range(0, len(players)):
        if players[x].playing():
            fullHands[x] = players[x].hand + table
            values.append(makeBestHand(fullHands[x]))
        else:
            print("Fold em")
            print()
            fullHands[x] = players[x].hand + table
            values.append(makeBestHand(fullHands[x]))
            values[x].folded()
    winner = list()
    printPowers(values)
    topHand(values, winner)
    w = winner[0]
    wins = 0
    wnum = 0
    winners = 0
    ws = list()
    for x in values:
        if x.power == w.power and sameHands(x.specs, w.specs):
            wnum = wins
            ws.append(wnum)
            winners += 1
        wins += 1
    if (winners == 1):
        print("hand " + str(wnum + 1) + " wins")
    elif (winners > 1):
        string = ""
        for x in ws:
            string = string + str(x + 1) + " "
        print("It be a draw and stuff between " + string)
    return ws