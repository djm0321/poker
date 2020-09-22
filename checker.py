from values import *
from collections import Counter
import operator
import utils

def findCard(hand, num):
    for x in hand:
        if x.number == num:
            return x

def aceStraightHigh(deck):
    aceDeck = list()
    for x in deck:
        aceDeck.append(x)
        if (x.number == 13):
            ace = utils.Card(x.suit, 0)
            aceDeck.append(ace)
    return aceDeck

def duplicates(hand, pairs, trips, quads):
    counts = Counter(card.number for card in hand)
    for num, times in counts.items():
        if times == 2:
            temp = findCard(hand, num)
            pairs.append(temp)
        elif times == 3:
            temp = findCard(hand, num)
            trips.append(temp)
        elif times == 4:
            temp = findCard(hand, num)
            quads.append(temp)
    pairs.sort(key = operator.attrgetter('number'), reverse = True)
    trips.sort(key = operator.attrgetter('number'), reverse = True)
    quads.sort(key = operator.attrgetter('number'), reverse = True)

def suitCounter(hand, suitCounts):
    counts = Counter(card.suit for card in hand)
    for suit, times in counts.items():
        suitCounts.append(times) 


def flushCheck(hand):
    flush = False
    flushSuit = -1
    counts = Counter(card.suit for card in hand)
    for suit, times in counts.items():
        if times >= 5:
            flush = True
            fSuit = suit
    return flush
            
def getFlush(hand, specs):
    flushSuit = -1
    counts = Counter(card.suit for card in hand)
    for suit, times in counts.items():
        if times >= 5:
            flushSuit = suit
    for x in hand:
        if x.suit == flushSuit:
            specs.append(x)
        if len(specs) == 5:
            break

def straightCheck(hand, specs):
    "check for a straight"
    strHand = list()
    strHand = hand
    strHand = aceStraightHigh(strHand)
    strHand = noDups(strHand)
    strHand.sort(key = operator.attrgetter('number'), reverse = True)
    i = 0
    straight = False
    straightHand = list()
    while i <= len(strHand) - 5:
        for x in range(i, i + 4):
            if strHand[x].number != strHand[x + 1].number + 1:
                break
            if x == i + 3:
                straight = True
                straightHand = strHand[i:i+5]
        if straight:
            break        
        i += 1
    for x in straightHand:
        specs.append(x)
    return straight

def straightFlushCheck(hand, specs):
    testHand = list()
    i = 0
    fSuit = 0
    if not flushCheck(hand):
        return False
    counts = Counter(card.suit for card in hand)
    for suit, times in counts.items():
        if times >= 5:
            flushSuit = suit
    for x in hand:
        if x.suit == fSuit:
            testHand.append(x)
    testHand = aceStraightHigh(testHand)
    testHand.sort(key = operator.attrgetter('number'), reverse = True)
    straight = False
    straightHand = list()
    while i <= len(testHand) - 5:
        for x in range(i, i + 4):
            if testHand[x].number != testHand[x + 1].number + 1:
                break
            if x == i + 3:
                straight = True
                straightHand = testHand[i:i+5]
                break
        if (straight == True):
            break
        i += 1
    for x in straightHand:
        specs.append(x)
    return straight


def fullHouseCheck(pairs, trips):
    fullHouse = False
    if len(pairs) > 0 and len(trips) > 0:
        fullHouse = True
    elif len(trips) > 1:
        fullHouse = True
    return fullHouse

def getFullHouse(specs, pairs, trips):
    if len(trips) == 1:
        for x in range(0, 5):
            if (x < 3):
                specs.append(trips[0])
            else:
                specs.append(pairs[0])
    else:
        for x in range(0, 5):
            if (x < 3):
                specs.append(trips[0])
            else:
                specs.append(trips[1])

def getDupHand(specs, hand, pairs, trips, quads):
    if(len(quads) > 0):
        for x in range(0, 4):
            specs.append(quads[0])
        highCards(specs, hand)
    elif(len(trips) > 0):
        for x in range(0, 3):
            specs.append(trips[0])
        highCards(specs, hand)
    elif(len(pairs) > 1):
        for x in range(0, 4):
            if x < 2:
                specs.append(pairs[0])
            else:
                specs.append(pairs[1])
        highCards(specs, hand)
    else:
        for x in range(0, 2):
            specs.append(pairs[0])
        highCards(specs, hand)

 

def highCards(specs, hand):
    inHand = False
    cardsInHand = len(specs)
    for x in hand:
        for i in specs:
            if (x.number == i.number) and (x.suit == i.suit):
                inHand = True
        if not inHand:
            specs.append(x)
            cardsInHand += 1
            if cardsInHand == 5:
                break
        inHand = False

def noDups(hand):
    "for straightCheck"
    noDupHand = list()
    dup = False
    for x in hand:
        for y in noDupHand:
            if x.number == y.number:
                dup = True
        if not dup:
            noDupHand.append(x)
        dup = False
    return noDupHand