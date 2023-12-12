def expansion(X, Y, Row, Column):
    n = len(Row)
    m = len(Column)
    Row1 = Row + [X[0]] + [Y[0]]
    SortedRow = sorted(range(len(Row1)), key = lambda index: Row1[index])
    id1 = SortedRow.index(n)
    id2 = SortedRow.index(n+1)
    
    Column1 = Column + [X[1]] + [Y[1]]
    SortedColumn = sorted(range(len(Column1)), key = lambda index: Column1[index])
    idc1 = SortedColumn.index(m)
    idc2 = SortedColumn.index(m+1)

    #First star
    Expansion_Constand = 2-1
    #Second star
    Expansion_Constand = 1000000-1
    
    return max(0,abs(id2-id1)-1)*Expansion_Constand + max(0,abs(idc2-idc1)-1)*Expansion_Constand

if __name__ == '__main__':
    with open('input11.txt') as f:
        arrayRaw = f.readlines()
        
    arrayRaw = [a.replace('\n','') for a in arrayRaw]
    RowExpansion = [i for i in range(len(arrayRaw)) if set(arrayRaw[i]) == {'.'}]
    ColumnExpansion = [i for i in range(len(arrayRaw[0])) if set([a[i] for a in arrayRaw]) == {'.'}]
    
    ListGalaxy = []
    for i in range(len(arrayRaw)):
        for j in range(len(arrayRaw[i])):
            if arrayRaw[i][j] == '#':
                ListGalaxy.append([i,j])
    boh=1
    Distance = []
    for i in range(len(ListGalaxy)):
        for j in range(i+1,len(ListGalaxy)):
            Distance.append(abs(ListGalaxy[i][0]-ListGalaxy[j][0])+abs(ListGalaxy[i][1]-ListGalaxy[j][1]) + expansion(ListGalaxy[i],ListGalaxy[j],RowExpansion.copy(),ColumnExpansion.copy()))
    print(sum(Distance))
