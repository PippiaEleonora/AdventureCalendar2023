import re
with open('input3.txt') as f:
    arrayRaw = f.readlines()
    
n = len(arrayRaw)
arrayRaw = [x.replace('\n','') for x in arrayRaw]
   
Numbers = [re.findall('[0-9]+',x) for x in arrayRaw]
Index = [[]]*n
for i in range(n):
    temp = arrayRaw[i]
    Index[i] = []
    for num in Numbers[i]:
        Index[i].append([temp.index(num), temp.index(num)+len(num)])
        temp = temp.replace(num,'.'*len(num),1)

Symbols = [[arrayRaw[i][max(0,numId[0]-1):min(numId[1]+1,len(arrayRaw[i]))]+arrayRaw[max(0,i-1)][max(0,numId[0]-1):min(numId[1]+1,len(arrayRaw[i]))]+arrayRaw[min(i+1,n-1)][max(0,numId[0]-1):min(numId[1]+1,len(arrayRaw[i]))] for numId in Index[i]] for i in range(n)]
Tot = 0
for i in range(n):
    Line = Symbols[i]
    for j in range(len(Line)):
        string = Line[j].replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','').replace('.','')
        if len(string)>0:
            Tot += int(Numbers[i][j])

print(Tot)

#Second Star
GearSymbol = [[i for i, ltr in enumerate(s) if ltr == '*'] for s in arrayRaw]
SymbolsAdj = [[arrayRaw[i][max(0,gearId-1):min(gearId+2,len(arrayRaw[i]))]+'.'+arrayRaw[max(0,i-1)][max(0,gearId-1):min(gearId+2,len(arrayRaw[i]))]+'.'+arrayRaw[min(i+1,n-1)][max(0,gearId-1):min(gearId+2,len(arrayRaw[i]))] for gearId in GearSymbol[i]] for i in range(n)]
Tot2 = 0
for i in range(n):
    for j in range(len(GearSymbol[i])):
        adjString = SymbolsAdj[i][j]
        if len(re.findall('[0-9]+',adjString))>1:
            column = GearSymbol[i][j]
            number = []
            if i == 0:
                for j in range(len(Index[i])):
                    if Index[i][j][0]<=column+1 and Index[i][j][1]>column-1:
                        number += [int(Numbers[i][j])]
                for j in range(len(Index[i+1])):
                    if Index[i+1][j][0]<=column+1 and Index[i+1][j][1]>column-1:
                        number += [int(Numbers[i+1][j])]
                Tot2 += number[0]*number[1]
            elif i == n-1:
                for j in range(len(Index[i-1])):
                    if Index[i-1][j][0]<=column+1 and Index[i-1][j][1]>column-1:
                        number += [int(Numbers[i-1][j])]
                for j in range(len(Index[i])):
                    if Index[i][j][0]<=column+1 and Index[i][j][1]>column-1:
                        number += [int(Numbers[i][j])]
                Tot2 += number[0]*number[1]
            else:
                for j in range(len(Index[i-1])):
                    if Index[i-1][j][0]<=column+1 and Index[i-1][j][1]>column-1:
                        number += [int(Numbers[i-1][j])]
                for j in range(len(Index[i])):
                    if Index[i][j][0]<=column+1 and Index[i][j][1]>column-1:
                        number += [int(Numbers[i][j])]
                for j in range(len(Index[i+1])):
                    if Index[i+1][j][0]<=column+1 and Index[i+1][j][1]>column-1:
                        number += [int(Numbers[i+1][j])]
                Tot2 += number[0]*number[1]
print(Tot2)
