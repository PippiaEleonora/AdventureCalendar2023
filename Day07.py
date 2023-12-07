
def getValue(card):
    # Five of a kind, where all five cards have the same label: AAAAA
    if len(set(card)) == 1:
        return 7
   
    elif len(set(card)) == 2:
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if len(card.replace(card[0],'')) in [1,4]:
            return 6
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        else:
            return 5
    elif len(set(card)) == 3:
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        shortCard = card.replace(card[0],'')
        if len(shortCard) == 3 or len(shortCard.replace(shortCard[0],'')) == 2:
            return 3
        else:
            return 4
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    elif len(set(card)) == 4:
        return 2
    else:
        # High card, where all cards' labels are distinct: 23456
        Order = [ord(c) if ord(c) < 58 else ord(c)-7 for c in card]
        if Order[0]+1 == Order[1] and Order[1]+1 == Order[2] and Order[2]+1 == Order[3] and Order[4]+1 == Order[5]:
            return 1
        else:
            return 0
        
def getValueJoker(card):
    # Five of a kind, where all five cards have the same label: AAAAA
    card_out_J = card.replace('1','')
    if len(set(card_out_J)) <= 1:
        return 7
   
    elif len(set(card_out_J)) == 2:
        # Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        if len(card_out_J)==2 or len(card_out_J)==3 or len(card_out_J.replace(card_out_J[0],'')) in [1,len(card_out_J)-1]:
            return 6
        # Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        else:
            return 5
    elif len(set(card_out_J)) == 3:
        # Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        # Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        shortCard = card_out_J.replace(card_out_J[0],'')
        if len(card_out_J)==5 and (len(shortCard) == 3 or len(shortCard.replace(shortCard[0],'')) == 2):
            return 3
        else:
            return 4
    # One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    elif len(set(card_out_J)) == 4:
        return 2
    else:
        # High card, where all cards' labels are distinct: 23456
        Order = [ord(c) if ord(c) < 58 else ord(c)-7 for c in card]
        if ((Order[0]+1 == Order[1] or card[0]=='1' or card[1]=='1') 
           and (Order[1]+1 == Order[2] or card[1]=='1' or card[2]=='1')
           and (Order[2]+1 == Order[3] or card[2]=='1' or card[3]=='1')
           and (Order[3]+1 == Order[4] or card[3]=='1' or card[4]=='1')):
            return 1
        else:
            return 0

if __name__ == '__main__':
    with open('input07.txt') as f:
        arrayRaw = f.readlines()
    
    n = len(arrayRaw)
    CardList = [card[0:5].replace('A','E').replace('K','D').replace('Q','C').replace('J','B').replace('T','A') for card in arrayRaw]
    Value = {CardList[i]: int(arrayRaw[i][6:]) for i in range(n)}
    CardList.sort()
    CardList.sort(key=getValue)
    TOT = 0
    for i in range(n):
        TOT += (i+1)*Value[CardList[i]]
    
    print(TOT)
    
    # Second star
    CardList = [card[0:5].replace('A','D').replace('K','C').replace('Q','B').replace('T','A').replace('J','1') for card in arrayRaw]
    Value = {CardList[i]: int(arrayRaw[i][6:]) for i in range(n)}
    CardList.sort()
    CardList.sort(key=getValueJoker)
    TOT = 0
    for i in range(n):
        TOT += (i+1)*Value[CardList[i]]
    print(TOT)

    
