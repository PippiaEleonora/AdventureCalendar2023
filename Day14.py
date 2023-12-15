import numpy as np
import time

def move_rocks(Platform):
    shape = Platform.shape
    n = shape[0]
    m = shape[1]

    for i in range(n):
        # start = time.time()   
        if 1 in Platform[i,:] and 0 in Platform[i,:] and -1 in Platform[i,:]:
            idBlockList = np.where(Platform[i,:] == -1)[1]
            idBlockList = np.append(idBlockList,m)
            idBlockList = np.insert(idBlockList,0,-1)
            for j in range(1,len(idBlockList)):
                index = idBlockList[j-1]+1
                total_one = (Platform[i,index:idBlockList[j]]*np.ones((idBlockList[j]-index,1)))[0,0]     
                Platform[i,index:index+int(total_one)] = np.ones((1,int(total_one)))
                Platform[i,index+int(total_one):idBlockList[j]] = Platform[i,index+int(total_one):idBlockList[j]]*0    
                  
        elif 1 in Platform[i,:] and 0 in Platform[i,:]:
            total_one = (Platform[i,:]*np.ones((m,1)))[0,0]     
            Platform[i,:int(total_one)] = np.ones((1,int(total_one)))
            Platform[i,int(total_one):] = Platform[i,int(total_one):]*0
    return Platform

def calculate_weight(Platform):
    shape = Platform.shape
    n = shape[0]
    Weight = 0
    for i in range(n):
        line = Platform[i]
        Weight += ((line>0)*np.transpose(line))[0,0]*(n-i)
    return Weight

if __name__ == '__main__':
    with open('input14.txt') as f:
        arrayRaw = f.readlines()
        
    arrayRaw = [[0 if a=='.' else 1 if a=='O' else -1 for a in Line.replace('\n','')] for Line in arrayRaw]
    
    #North
    Platform = np.transpose(np.matrix(arrayRaw))
    Platform = move_rocks(Platform)
    Platform = np.transpose(Platform)
    print(calculate_weight(Platform))
    
    #Second star
    iteration = 1000000000
    Platform = np.matrix(arrayRaw)
    Start_Platform = [Platform.copy()]
    i = 0
    repetition = 0
    while i < iteration and not repetition:
        print(i)
        #North
        Platform = np.transpose(Platform)
        Platform = move_rocks(Platform)

        #West
        Platform = np.transpose(Platform)
        Platform = move_rocks(Platform)
        
        #South
        Platform = np.flip(np.transpose(Platform),1)
        Platform = move_rocks(Platform)
        
        #East
        Platform = np.flip(np.transpose(Platform),1)
        Platform = move_rocks(Platform)
        
        Platform = np.flip(np.flip(Platform,0),1)
        
        if any([(savePlat == Platform).all() for savePlat in Start_Platform]):
            repetition = 1
        else:
            Start_Platform.append(Platform.copy())
            i +=1
        
    idStart = list([(savePlat == Platform).all() for savePlat in Start_Platform]).index(True) -1
    FinalPlat = (iteration-idStart-1)%(i-idStart) + idStart + 1
    print(calculate_weight(Start_Platform[FinalPlat]))
    
    
    # start = time.time()
    # end = time.time()
    # print(end - start)