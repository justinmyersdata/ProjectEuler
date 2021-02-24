
def pairlist(x):
    final = []
    pairs = {}
    
    for number in x:
        if number in pairs.keys():
            pairs[number] += 1
        else:
            pairs[number] = 1
    
    pair_list =  list(pairs.items())
    
    for pair in pair_list:
        temp = []
        if pair[1] == 4:
            temp.append(pair[0])
        temp.sort()
        final += temp
        
    for pair in pair_list:
        temp = []
        if pair[1] == 3:
            temp.append(pair[0])
        temp.sort()
        final += temp
        
    for pair in pair_list:
        temp = []
        if pair[1] == 2:
            temp.append(pair[0])
        temp.sort()
        final += temp
        
    for pair in pair_list:
        temp = []
        if pair[1] == 1:
            temp.append(pair[0])
        temp.sort()
        final += temp
        
    return final

def cardrankings(x):
    if x[0] == 'T':
        return '10'+x[1]
    elif x[0] == 'J':
        return '11'+x[1]
    elif x[0] == 'Q':
        return '12'+x[1]
    elif x[0] == 'K':
        return '13'+x[1]
    elif x[0] == 'A':
        return '14'+x[1]
    else:
        return(x)
        


def gethands():
    with open(r'C:\Users\myersj1\Desktop\poker.txt','r') as f:
        hands = f.readlines()
        
    for ind,hand in enumerate(hands):
        hands[ind] = hand.replace('\n','').split(' ')
    
    hands1 = []
    hands2 = []
    for hand in hands:
        hands1.append(hand[:5])
        hands2.append(hand[5:])
        
    for ind,hand in enumerate(hands1):
        for i,card in enumerate(hand):
            hands1[ind][i] = cardrankings(card)
            
    for ind,hand in enumerate(hands2):
        for i,card in enumerate(hand):
            hands2[ind][i] = cardrankings(card)
    
    hands = list(zip(hands1,hands2))
    return(hands)

def handrankings(cards):
    cardnum = [int(x[:-1]) for x in cards]
    cardsuit = list(set([x[-1:] for x in cards]))
    cardnum.sort(reverse=True)
    
    straight = True
    for ind,num in enumerate(cardnum[:-1]):
        if cardnum[ind]-1!=cardnum[ind+1]:
            straight = False
            break
    
    pairs = {}
    for card in cardnum:
        if card in pairs.keys():
            pairs[card] += 1
        else:
            pairs[card] = 1
    
    flush = True
    if len(cardsuit)>1:
        flush = False
        
    #Straight Flush
    if flush and straight:
        value = 10
        
    #Four of a kind
    elif 4 in pairs.values():
        value = 9
        
    #Full House
    elif 3 in pairs.values() and 2 in pairs.values():
        value = 8
    #Flush
    elif flush:
        value = 7
    #Straight
    elif straight:
        value = 6
    
    elif 3 in pairs.values():
        value = 5
    
    elif 2 in pairs.values():
        #2 Pair
        if len(list(set(cardnum))) == 3:
            value = 4
        #1 Pair
        else:
            value = 3
    else:
        value = 2
    return(value,pairlist(cardnum))

def handrankingcompare(hand1,hand2):
    h1value, h1cards = handrankings(hand1)
    h2value, h2cards = handrankings(hand2)
    #return(h1value,h1cards,h2value,h2cards)
    if h1value > h2value:
        return 1
    elif h1value < h2value:
        return 2
    else:
        for card in range(len(h1cards)):
            if h1cards[card] > h2cards[card]:
                return 1
            elif h1cards[card] < h2cards[card]:
                return 2
        return 0
    
                
hands = gethands()
player1 = 0
winner = []
for hand in hands:
    winner.append(handrankingcompare(hand[0],hand[1]))
    
total = 0
for win in winner:
    if win == 1:
        total+=1
print(total)

##Have to represent who has the highest pair