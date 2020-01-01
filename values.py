
class handValue():
    "denotes the value of a hand"
    def __init__(self, power, specs):
        self.power = power
        self.specs = specs

def compareHands(h1, h2):
    # print(h1.power)
    # print(h2.power)
    if(h1.power > h2.power):
        # print("hand 1 is more powerful")
        return h1
    elif(h2.power > h1.power):
        # print("hand 2 is more powerful")
        return h2
    elif(h2.power == h1.power):
        return compareSpecs(h1, h2)

def compareSpecs(h1, h2):
    # for x in h1.specs:
    #     print(x.number)
    # for x in h2.specs:
    #     print(x.number)
    for i in range(0, len(h1.specs)):
        if h1.specs[i].number > h2.specs[i].number:
            # print("hand 1 wins")
            return h1
            break
        elif h2.specs[i].number > h1.specs[i].number:
            # print("hand 2 wins")
            return h2
            break
        elif i == len(h1.specs) - 1:
            print("it be a draw n stuff")
            return h1

def topHand(handList, winner):
    hi = 0
    winList = list()
    if len(handList) % 2 == 0:
        while hi < len(handList):
            winList.append(compareHands(handList[hi], handList[hi+1]))
            hi += 2
        topHand(winList, winner)
    elif len(handList) == 1:
        winner.append(handList[0])
    else:
        while hi < len(handList) - 1:
            winList.append(compareHands(handList[hi], handList[hi+1]))
            hi += 2
        winList.append(handList[len(handList) - 1])
        topHand(winList, winner)

def printPowers(hands):
    for x in hands:
        print(x.power)

def sameHands(h1, h2):
    for x in range (0, len(h1)):
        if h1[x].number != h2[x].number:
            return False
    return True