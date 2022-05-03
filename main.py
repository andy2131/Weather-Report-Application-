f=open('weather_data.dat','r')
result=[line.split(',') for line in f]


def duplicate(result):
    newresult=[]
    for i in result:
        if i not in newresult:
            newresult.append(i)
    return newresult

def format(newresult):
    for i in range(len(newresult)):
        if type(newresult[i])==list:
            for j in range(len(newresult[i])):
                newresult[i][j]=float(newresult[i][j])
    return newresult

def month(newresult):
    for i in range(len(newresult)):
        if newresult[i][0]==1:
            newresult[i][0]='Jan'
        if newresult[i][0]==2:
            newresult[i][0]='Feb'
        if newresult[i][0]==3:
            newresult[i][0]='Mar'
        if newresult[i][0]==4:
            newresult[i][0]='Apr'
        if newresult[i][0]==5:
            newresult[i][0]='May'
        if newresult[i][0]==6:
            newresult[i][0]='Jun'
    return newresult


a=duplicate(result)
b=format(a)
temp=(month(b))

import weatherstat
x=weatherstat.temp_convert(temp)

def dictionary(x):
    dict={}
    for i in range(len(x)):
        dict[x[i][0]]=x[i][1:]
    return dict

dict=dictionary(x)
average=weatherstat.average(dict)
highlow=weatherstat.highlow(dict)

def write(dict):
    f=open('weathreport.txt','a')
    for k,v in dict.items():
        f.write(k+':'+str(v).strip('[]')+'\n')
    f.write('Month\t'+'average temp(c)\t'+'high,low(c)')
    for k,v in average.items():
        f.write('\n'+k+'\t'+str(v)+'\t\t'+str(highlow[k]).strip('()'))
    return

write(dict)





        

 



        
         
    



            
    
        
  

