"""
このファイルに解答コードを書いてください
"""
file=open('input.txt','r',encoding='UTF-8')
data=file.readlines()
num=int(data[-1])
#print(num)
data.pop(-1)
data1=[]
data2=[]
for s in data:
    x=s.split(':')
    data1.append(int(x[0]))
    data2.append(x[1])
i=0
j=0

for i in range(53):
    for j in range(52):
        if data1[j] > data1[j+1]:
            sort=data1[j]
            data1[j]=data1[j+1]
            data1[j+1]=sort
            sort2=data2[j]
            data2[j]=data2[j+1]
            data2[j+1]=sort2
i=0
result=''
#print(type(num))
#print(type(data1[i]))
for i in range (53):
    if num%data1[i]==0:
        result+=data2[i]
    else:
        result=result+str(data1[i])
print(result)
file.close()