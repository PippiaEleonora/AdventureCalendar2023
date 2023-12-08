
with open('/uploads/Input08.txt') as f:
    arrayRaw = f.readlines()
Graph ={}

arrayRaw = arrayRaw[0].split(')') 
print(arrayRaw[0][-5:-1])
for i in range(2,len(arrayRaw)):
    r = arrayRaw[i]
    Graph.update({r[1:4]: (r[8:11], r[13:16]) } )
    
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
    
