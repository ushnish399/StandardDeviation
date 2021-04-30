import csv
with open("../DataSets/Data1.csv", newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

data=filedata[0]
print(data)
n=len(data)
sum=0
sum1=0
a=0
for i in data:
    sum=sum+int (i)

mean=sum/n
squaredlist=[]
for i in data:
   a= int(i)-mean
   a=a**2
   squaredlist.append(a)
   sum1=sum1+a

result=sum1/n
import math
standardDeviation=math.sqrt(result)
print(standardDeviation)





