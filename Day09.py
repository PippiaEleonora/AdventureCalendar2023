from math import factorial
import re
import pandas as pd

def Pascal_number(n,r):   
    return factorial(n)/(factorial(n-r)*factorial(r))

if __name__ == '__main__':
    with open('input09.txt') as f:
        arrayRaw = f.readlines()
        
    OASIS = [x.replace('\n','').split(' ') for x in arrayRaw]
    OASIS = [[int(n) for n in Num] for Num in OASIS]
    Prediction = []
    for i in range(len(OASIS)):
        signal = OASIS[i]
        Prediction += [signal[-1]]
        vector = pd.Series(signal)
        while any(vector):
            vector = vector[1:].reset_index(drop=True).subtract(vector[0:len(vector)-1].reset_index(drop=True))
            if any(vector):
                Prediction[i] += vector.iloc[-1]

    print(sum(Prediction))
    
    # Second star
    Prediction = []
    for i in range(len(OASIS)):
        signal = OASIS[i]
        Prediction += [signal[0]]
        vector = pd.Series(signal)
        curr = 0
        while any(vector):
            vector = vector[1:].reset_index(drop=True).subtract(vector[0:len(vector)-1].reset_index(drop=True))
            if any(vector):
                if curr == 0:
                    Prediction[i] -= vector.iloc[0]
                    curr = 1
                else:
                    Prediction[i] += vector.iloc[0]
                    curr = 0 

    print(sum(Prediction))