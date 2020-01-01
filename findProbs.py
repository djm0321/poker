# So this is how this is gonna work
# First (1st): Check to see if thing exists within cards
# Second (2nd): If thing exists, 100% chance (duh). If not, check what would be needed to satisfy said thing
# 3rd (third): divide number of cards needed by number of unknown cards (52 - number of cards known) to get probability of thing occuring
# Fourth (4th): Finish the rest in winProb.py

import random
import operator
import math
from collections import Counter
import utils
import checker
import values

def pairProb(hand):
    cards = len(hand)
    cardsLeft = 7 - cards
    possiblePairs = cards * cardsLeft
    totalCards = 52.0 - cards
    if (cards == 6):
        return (cards * 3.0) / totalCards
    elif (cards == 7):
        return 0
    else:
        return ((cards * 3.0) / totalCards) + ((13.0 - cards) * (12.0 / 2652))

def twoPairProb(hand, pairs):
    cards = len(hand)
    cardsLeft = 7 - cards
    totalCards = 52.0 - cards
    if (len(pairs) > 0):
        cardsLeftPaired = cards - 2
        if (cards >= 6):
            return (cardsLeftPaired * 3.0) / totalCards
        else:
            return ((cardsLeftPaired * 3.0) / totalCards) + ((13.0 - cards - 1) * (12.0 / 2652))
    else:
        if (cards >= 6):
            return 0
        elif (cards == 5):
            return ((cards * 3.0) / totalCards) * ((cards - 1) * 3.0 / totalCards)
        else:
            print("sadness")
            

def checkProbs(hand, probabilities):
    "Checks for existance of things. If exists, returns 1 in probabilities array. If not, finds probability that it will"
    sFlush = [None] * 5
    straight = [None] * 5
    flush = [None] * 5
    fullHouse = [None] * 5
    pairs = list()
    trips = list()
    quads = list()
    checker.duplicates(hand, pairs, trips, quads)
    if checker.straightFlushCheck(hand, sFlush):
        probabilities[0] = 1
    else:
        print("probability of straight flush happening")
    if len(quads) > 0:
        probabilities[1] = 1
    else:
        print("probability of getting quads")
    if checker.fullHouseCheck(pairs, trips):
        probabilities[2] = 1
        checker.getFullHouse(fullHouse, pairs, trips)
    else:
        print("probability of a full house")
    if checker.flushCheck(hand):
        probabilities[3] = 1
        checker.getFlush(hand, flush)
    else:
        print("probability of a flush")
    if checker.straightCheck(hand, straight):
        probabilities[4] = 1
    else:
        print("probability of a straight")
    if len(trips) + len(quads) > 0:
        probabilities[5] = 1
    else:
        print("probability of trips")
    if len(pairs) + len(trips) + len(quads) > 1:
        probabilities[6] = 1
    else:
        print("probability of 2 pairs")
    if len(pairs) + len(trips) + len(quads) > 0:
        probabilities[7] = 1
    else:
        print("probability of pairs")