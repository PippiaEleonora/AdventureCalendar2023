import re
with open('input4.txt') as f:
    arrayRaw = f.readlines()
    
n = len(arrayRaw)
Lists = [ x.split('|') for x in arrayRaw]
ListGame = [x[0].split(':')[1] for x in Lists]
ListGame = [set(re.findall('[0-9]+',x)) for x in ListGame]
ListWin = [set(re.findall('[0-9]+',x[1])) for x in Lists]
WinningVal = [2**(len(ListGame[i]) - len(ListGame[i]-ListWin[i])-1) if len(ListGame[i]) - len(ListGame[i]-ListWin[i])>0 else 0 for i in range(n)]
print(sum(WinningVal))

# Second star
WinningValPerCard = [(len(ListGame[i]) - len(ListGame[i]-ListWin[i])) for i in range(n)]
WinningCards = [1]*n
for i in range(n):
    for j in range(WinningValPerCard[i]):
        if i+j+1<n:
            WinningCards[i+j+1] += WinningCards[i]
print(sum(WinningCards))
