def temp_convert(temp):
    for i in range(len(temp)):
        if type(temp[i])==list:
            for j in range(len(temp[i])):
                if type(temp[i][j])==float:
                    temp[i][j]=round((temp[i][j]-32)*5/9,1)
    return temp

def average(temp):
    avgdict={}
    for k,v in temp.items():
        avgdict[k]=round(sum(v)/float(len(v)),1)
    return avgdict

def highlow(temp):
    highlowdict={}
    for k,v in temp.items():
        highlowdict[k]=max(v),min(v)
    return highlowdict

    

            
        
        
    
