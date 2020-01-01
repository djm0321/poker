import random
import math
from checker import *
from values import *
class Card(): 
    "creating a card with a suit and card value (created to help straight flushes)"
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def returnCard(self):
        print("this card is the " + str(self.number) + " of " + str(self.suit))

def dealHand(deck): 
    a = deck.pop()
    b = deck.pop()
    return [a, b]

def dealTable(deck):
    a = 0
    table = list()
    while a < 5:
        table.append(deck.pop())
        a+=1
    return table

def dealFlop(deck):
    table = list()
    for x in range(0, 3):
        table.append(deck.pop())
    return table

def dealR(deck, table):
    table.append(deck.pop())

def getSuits(num):
    "gets suits of cards"
    suits = list()
    for x in num:
        suits.append(math.floor(x/13))
    return suits

def getNums(num):
    "gets numbers of cards"
    nums = list()
    for x in num:
        nums.append(x%13)
    return nums

def makeCard(num):
    card = Card(math.floor(num/13), (num%13))
    return card

def deckToCards(deck):
    newDeck = list()
    for x in deck:
        if x%13 == 0:
            newDeck.append(Card(math.floor(x/13), 13))
        else:
            newDeck.append(makeCard(x))
    sortDeck(newDeck)
    return newDeck

def makeBestHand(hand):
    power = int
    specs = list()
    fSuit = int
    pairs = list()
    trips = list()
    quads = list()
    duplicates(hand, pairs, trips, quads)
    if straightFlushCheck(hand, specs):
        power = 8
    elif len(quads) > 0:
        getDupHand(specs, hand, pairs, trips, quads)
        power = 7
    elif fullHouseCheck(pairs, trips):
        power = 6
        getFullHouse(specs, pairs, trips)
    elif flushCheck(hand):
        power = 5
        getFlush(hand, specs)
    elif straightCheck(hand, specs):
        power = 4
    elif len(trips) > 0:
        getDupHand(specs, hand, pairs, trips, quads)
        power = 3
    elif len(pairs) > 1:
        getDupHand(specs, hand, pairs, trips, quads)
        power = 2
    elif len(pairs) == 1:
        getDupHand(specs, hand, pairs, trips, quads)
        power = 1
    else:
        highCards(specs, hand)
        power = 0
    return handValue(power, specs)
    

    
    


def sortDeck(hand):
    hand.sort(key = operator.attrgetter('number'), reverse = True)
    