def HASHprogram(string:str):
    Value = 0
    for s in string:
        Value += ord(s)
        Value *= 17
        Value = Value%256
    return Value

if __name__ == '__main__':
    with open('input15.txt') as f:
        arrayRaw = f.readlines()
        
    arrayRaw = arrayRaw[0].replace('\n','')
    InputString = arrayRaw.split(',')
    ValueList = []
    for i in InputString:
        ValueList.append(HASHprogram(i))
        
    print(sum(ValueList))
    
    # Second star
    ValueList = []
    LensPlaces = {}
    LensVal = {}
    Boxes = {}
    for i in InputString:
        if '=' in i:
            label = i.split('=')
            boxnumb = HASHprogram(label[0])
            if boxnumb in list(Boxes.keys()):
                if label[0] in list(LensPlaces.keys()):
                    if LensPlaces[label[0]] == boxnumb:
                        LensVal[label[0]] = int(label[1])
                    else:
                        Boxes[boxnumb].append(label[0])
                        LensVal[label[0]] = int(label[1])
                        LensPlaces[label[0]] = boxnumb
                else:
                    Boxes[boxnumb].append(label[0])
                    LensVal.update({label[0]: int(label[1])})
                    LensPlaces.update({label[0]: boxnumb})
            else:
                Boxes.update({boxnumb: [label[0]]})
                LensPlaces.update({label[0]: boxnumb})
                LensVal.update({label[0]: int(label[1])})
        else:
            boxnumb = HASHprogram(i.replace('-',''))
            if i.replace('-','') in list(LensPlaces.keys()):
                if LensPlaces[i.replace('-','')] == boxnumb:
                    Boxes[boxnumb].remove(i.replace('-',''))
                    LensPlaces[i.replace('-','')] = -1
        
    Total = 0
    for len in list(LensPlaces.keys()):
        if LensPlaces[len]>=0:
            Total += (1+LensPlaces[len])*(Boxes[LensPlaces[len]].index(len)+1)*LensVal[len]
    print(Total)