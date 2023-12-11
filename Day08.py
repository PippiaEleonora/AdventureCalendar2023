import math

def mcm_multiplo(Numbers):
    Curr = Numbers[0]
    for i in range(1,len(Numbers)):
        Curr = int((Curr*Numbers[i])/math.gcd(Curr,Numbers[i]))
        
    return Curr

if __name__ == '__main__':
    with open('input08.txt') as f:
        arrayRaw = f.readlines()
    Graph ={}

    for i in range(2,len(arrayRaw)):
        r = arrayRaw[i]
        Graph.update({r[0:3]: (r[7:10], r[12:15]) } )
        
    Node = 'AAA'
    Count = 0
    i = 0
    Instruction = arrayRaw[0].replace('\n','').replace('L','0').replace('R', '1')
    #print(Instruction)
    #print(Graph['AAA'])
    while not Node == 'ZZZ':
        Node = Graph[Node][int(Instruction[i])]
        Count += 1
        i += 1
        if i == len(Instruction):
            i = 0
            
    print(Count)

    #Second star
    NodeList = [n for n in list(Graph.keys()) if n[-1] == 'A']
    EndList = [n for n in list(Graph.keys()) if n[-1] == 'Z']

    CountList = [0]*len(NodeList)
    for j in range(len(NodeList)):
        n = NodeList[j]
        i = 0
        while not n[-1] == 'Z':
            n = Graph[n][int(Instruction[i])] 
            CountList[j] += 1
            i += 1
            if i == len(Instruction):
                i = 0
        
    
    print(mcm_multiplo(CountList))


