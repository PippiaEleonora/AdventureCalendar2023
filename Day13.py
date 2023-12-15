import numpy as np
if __name__ == '__main__':
    with open('input12.txt') as f:
        arrayRaw = f.readlines()
    
    
    FrameList = []
    Matrix = []
    for i in range(len(arrayRaw)):
        if arrayRaw[i] == '\n':
            FrameList.append(Matrix.copy())
            Matrix = []
        else:
            line = np.array([1 if a=='#' else 0 for a in arrayRaw[i].replace('\n','')])
            if Matrix == []:
                Matrix = np.matrix([line])
            else:
                Matrix = np.concatenate((Matrix, np.matrix([line])),axis=0)
    FrameList.append(Matrix.copy())
    
    ColumnMirror = [0]*len(FrameList)
    RowMirror = [0]*len(FrameList)
    tollerance = 1
    for k in range(len(FrameList)):
        f = FrameList[k]
        i = 1
        j = 1
        while i < f.shape[0]:
            if i > f.shape[0]/2:
                if sum(np.transpose(sum((f[i:,:] == f[i-1:2*i-f.shape[0]-1:-1,:])))).item(0) == f[i:,:].size - tollerance:
                    RowMirror[k] = i
                    i = f.shape[0]
                    j = f.shape[1]
                else:
                    i += 1
            else:
                if sum(np.transpose(sum((f[0:i,:] == f[2*i-1:i-1:-1,:])))).item(0) == f[0:i,:].size - tollerance:
                    RowMirror[k] = i
                    i = f.shape[0]
                    j = f.shape[1]
                else:
                    i += 1
            
        
        while j < f.shape[1]:
            if j > f.shape[1]/2:
                if sum(np.transpose(sum((f[:,j:] == f[:,j-1:2*j-f.shape[1]-1:-1])))).item(0) == f[:,j:].size - tollerance:
                    ColumnMirror[k] = j
                    j = f.shape[1]
                else:
                    j += 1
            else:
                if sum(np.transpose(sum((f[:,0:j] == f[:,2*j-1:j-1:-1])))).item(0) == f[:,0:j].size - tollerance:
                    ColumnMirror[k] = j
                    j = f.shape[1]
                else:
                    j += 1

    print(sum(RowMirror)*100 + sum(ColumnMirror))