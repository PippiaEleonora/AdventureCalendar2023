import numpy
import math
import re

def numbSolution(time, destination):
    # x^2 -timeX + destination < 0
    #
    epsilon = 0.0000001
    delta = time**2 -4*destination
    if delta<=0:
        return 0
    else:
        left = math.ceil((time -math.sqrt(delta))/2+epsilon)
        right = math.floor((time +math.sqrt(delta))/2-epsilon)
        return right-left+1

if __name__ == '__main__':
    with open('input06.txt') as f:
        arrayRaw = f.readlines()
        
        Numbers = [re.findall('[0-9]+',x) for x in arrayRaw]  
        
        Tot = []
        for i in range(len(Numbers[0])):
            Tot.append(numbSolution(int(Numbers[0][i]), int(Numbers[1][i])))
        
        print(numpy.prod(Tot))
        
        CompleteRace = numbSolution(int(''.join(Numbers[0])), int(''.join(Numbers[1])))
        print(CompleteRace)
        
        