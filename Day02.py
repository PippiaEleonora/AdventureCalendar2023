import re
with open('input02.txt') as f:
    arrayRaw = f.readlines()
BlueBlocks = [ re.findall('([0-9]+) (blue)', x) for x in arrayRaw]
BlueBlocks = [[int(b[0]) for b in bLine] for bLine in BlueBlocks]
RedBlocks = [ re.findall('([0-9]+) (red)', x) for x in arrayRaw]
RedBlocks = [[int(r[0]) for r in rLine] for rLine in RedBlocks]
GreenBlocks = [ re.findall('([0-9]+) (green)', x) for x in arrayRaw]
GreenBlocks = [[int(g[0]) for g in gLine] for gLine in GreenBlocks]
n = len(arrayRaw)


maxR = 12
maxG = 13
maxB = 14

FeasibleGames = [i+1 if max(BlueBlocks[i])<=maxB and max(RedBlocks[i])<=maxR and max(GreenBlocks[i])<=maxG else 0 for i in range(n)]
print(sum(FeasibleGames))

# Second star
MaxBlocks =[max(BlueBlocks[i])*max(RedBlocks[i])*max(GreenBlocks[i]) for i in range(n)]
print(sum(MaxBlocks))
