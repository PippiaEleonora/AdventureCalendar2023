import math
import numpy as np
if __name__ == '__main__':
    with open('input10.txt') as f:
        arrayRaw = f.readlines()
        
    r = 0
    found = 0
    c = 0
    while r<len(arrayRaw) and not found:
        if 'S' in arrayRaw[r]:
            found = 1
            c = arrayRaw[r].find('S')
        else:
            r += 1    
    
    movements = {'F': lambda new,prev :[-(new[1]-prev[1]), -(new[0]-prev[0])],
                 'J': lambda new,prev :[-(new[1]-prev[1]), -(new[0]-prev[0])],
                 '7': lambda new,prev :[new[1]-prev[1], new[0]-prev[0]],
                 'L': lambda new,prev :[new[1]-prev[1], new[0]-prev[0]],
                 '-': lambda new,prev :[0, new[1]-prev[1]],
                 '|': lambda new,prev :[new[0]-prev[0], 0]}
    
    count = 0
    prev = [r, c]
    # The starting point is custom, look ad your input and define the direction
    start = [r,c+1]
    while not start == [r,c]:
        count += 1
        old = start.copy()
        motion = movements[arrayRaw[start[0]][start[1]]](start,prev)
        start[0] += motion[0]
        start[1] += motion[1]
        prev = old
    print(math.ceil(count/2))
        
    # Second star
    Values =    {'F': np.matrix([[0,1],[-1,0]]),
                 'J': np.matrix([[0,1],[-1,0]]),
                 '7': np.matrix([[0,1],[1,0]]),
                 'L': np.matrix([[0,1],[1,0]]),
                 '-': np.matrix([[1,0],[0,1]]),
                 '|': np.matrix([[1,0],[0,1]])}

    DrawVal = {str(np.array([[1,0]])): '>',
               str(np.array([[-1,0]])): '<',
               str(np.array([[0,1]])): '^',
               str(np.array([[0,-1]])): 'v'}
    
    Matrix_Value = []
    Matrix = []
    Drawing1 = []
    Drawing2 = []
    for i in range(len(arrayRaw)):
        Matrix += [[0]* len(arrayRaw[0])]
        Drawing1 += [['0']* len(arrayRaw[0])]
        Drawing2 += [['0']* len(arrayRaw[0])]
        Matrix_Value += [[np.zeros(2)]* len(arrayRaw[0])]
        
    # The starting point is custom, look ad your input and define the direction
    Matrix_Value[r][c+1] = np.matrix([[0,1],[0,1]])
    Matrix[r][c] = 1
    Drawing1[r][c+1] = '^'
    Drawing2[r][c] = 'S'
    prev = [r, c]
    start = [r,c+1]
    
    
    while not start == [r,c]:
        old = start.copy()
        motion = movements[arrayRaw[start[0]][start[1]]](start,prev)
        
        Matrix[start[0]][start[1]] = 1
        Drawing2[start[0]][start[1]] = arrayRaw[start[0]][start[1]]
        start[0] += motion[0]
        start[1] += motion[1]
        prev = old
        if not start == [r,c]:
            sign = 1
            if (arrayRaw[start[0]][start[1]] == 'F' and motion[0] == 0) or (arrayRaw[start[0]][start[1]] == 'J' and motion[0] == 0):
                sign = -1
            
            vect = Matrix_Value[prev[0]][prev[1]][1]
            new_vect = np.transpose(sign*Values[arrayRaw[start[0]][start[1]]]*np.transpose(vect))
            Matrix_Value[start[0]][start[1]] = np.concatenate((vect, new_vect), axis = 0)
            Drawing1[start[0]][start[1]] = DrawVal[str(new_vect)]
        
        
    path = sum([sum(m) for m in Matrix])
    count = 0

    for i in range(len(Matrix)):
        if sum(Matrix[i])<len(Matrix[i]) and any(Matrix[i]):
            j = Matrix[i].index(1)
            j_prev = j
            while j < len(Matrix[i]):
                if not Matrix[i][j]:
                    if Matrix[i-1][j] and any(Matrix[i][j:]):
                        j_prev = j                    
                        j += Matrix[i][j:].index(1)
                        if Matrix_Value[i-1][j_prev].item(0) == 0 and Matrix_Value[i-1][j_prev].item(1) == 0:
                            Matrix[i][j_prev:j] = [1]*(j-j_prev)
                            Drawing1[i][j_prev:j] = ['.']*(j-j_prev)
                            Drawing2[i][j_prev:j] = ['.']*(j-j_prev)
                            count += (j-j_prev)
                        elif Matrix_Value[i][j_prev-1].item(0)<=0 and Matrix_Value[i][j].item(0)>=0 and Matrix_Value[i][j_prev-1].item(2)<=0 and Matrix_Value[i][j].item(2)>=0 and all([m.item(1)>=0 for m in Matrix_Value[i-1][j_prev:j]]) and all([m.item(1)<=0 for m in Matrix_Value[i+1][j_prev:j]]):  
                            Matrix[i][j_prev:j] = [1]*(j-j_prev)
                            Drawing1[i][j_prev:j] = ['.']*(j-j_prev)
                            Drawing2[i][j_prev:j] = ['.']*(j-j_prev)
                            count += (j-j_prev)
                        else:
                            j += Matrix[i][j:].index(1)
                    else:
                        if 1 in Matrix[i][j:]:
                            j += Matrix[i][j:].index(1)
                        else:
                            j = len(Matrix[i])
                else:
                    j += 1
                    j_prev = j
    print(sum([sum(m) for m in Matrix]) - path)
    Drawing1 = [' '.join(d) for d in Drawing1]
    with open('prova1.txt', 'w') as f:
        f.write('\n'.join(Drawing1))
        
    Drawing2 = [' '.join(d) for d in Drawing2]
    with open('prova2.txt', 'w') as f:
        f.write('\n'.join(Drawing2))