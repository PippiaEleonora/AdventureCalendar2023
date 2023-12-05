import re
import math
with open('input1.txt') as f:
    arrayRaw = f.readlines()
coordinates = [ re.findall('[0-9]', x) for x in arrayRaw]
realcoodinates = [ int(coo[0]+coo[-1]) for coo in coordinates]
print(sum(realcoodinates))

# Second start
substring = ['one','1','two','2','three','3','four','4','five','5','six','6','seven','7','eight','8','nine','9']
indexSubstring_MIN = [[x.find(y) if x.find(y)>=0 else 100000 for y in substring ] for x in arrayRaw]
indexSubstring_MAX = [[x[::-1].find(y[::-1]) if x[::-1].find(y[::-1])>=0 else 100000 for y in substring ] for x in arrayRaw]
decimalVal = [(math.floor(idMIN.index(min(idMIN))/2)+1)*10 for idMIN in indexSubstring_MIN]
unitVal = [math.floor(idMAX.index(min(idMAX))/2)+1 for idMAX in indexSubstring_MAX]

print(sum(decimalVal)+sum(unitVal))
