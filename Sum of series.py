import math
x=int(input("Enter a number: "))
n=int(input("Enter steps: "))
sum=0
for i in range(1,n+1):
    p=math.pow(x,i*2)
    sum=sum+p
print("sum: ",sum)
