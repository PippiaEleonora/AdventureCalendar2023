import re
import pandas as pd

with open('input05.txt') as f:
    arrayRaw = f.readlines()
  
Numbers = [re.findall('[0-9]+',x) for x in arrayRaw]  
n = len(Numbers)

curr = 0
first = 0
ConversionMap = [{}]
for i in range(3,n):
    if Numbers[i] == [] and first == 0:
        first = 1
        curr += 1
        ConversionMap += [{}]
    elif Numbers[i] != []:
        first = 0
        ConversionMap[curr].update({pd.Interval(int(Numbers[i][1]),int(Numbers[i][1])+int(Numbers[i][2]),closed='left'): int(Numbers[i][0])-int(Numbers[i][1])})

# First star
DestinationSeeds = [int(num) for num in Numbers[0]]

nSeed = len(DestinationSeeds)
for i in range(len(ConversionMap)):    
        for j in range(nSeed):
            conversion = 0
            for key in list(ConversionMap[i].keys()):
              if DestinationSeeds[j] in key and not conversion:
                  conversion = 1
                  DestinationSeeds[j] += ConversionMap[i][key]
print(min(DestinationSeeds))


# Second star
DestinationSeeds = []
for i in range(len(Numbers[0])):
    if i%2 == 1:
        DestinationSeeds += [pd.Interval(int(Numbers[0][i-1]),int(Numbers[0][i-1])+int(Numbers[0][i]),closed='left')]
        
for i in range(len(ConversionMap)):
    j = 0    
    while j <len(DestinationSeeds):
        conversion = 0
        for key in list(ConversionMap[i].keys()):
            if DestinationSeeds[j].overlaps(key) and not conversion:
                conversion = 1
                if DestinationSeeds[j] in key:
                    DestinationSeeds[j] = pd.Interval(DestinationSeeds[j].left + ConversionMap[i][key],DestinationSeeds[j].right + ConversionMap[i][key],closed='left')
                else:
                    Left = DestinationSeeds[j].left
                    Right = DestinationSeeds[j].right
                    if Left < key.left:
                        DestinationSeeds += [pd.Interval(Left,key.left,closed='left')] 
                        Left = key.left
                    if Right > key.right:
                        DestinationSeeds += [pd.Interval(key.right,Right,closed='left')]
                        Right = key.right
                    DestinationSeeds[j] = pd.Interval(Left + ConversionMap[i][key],Right + ConversionMap[i][key],closed='left')
        j += 1
print(min([d.left for d in DestinationSeeds]))
