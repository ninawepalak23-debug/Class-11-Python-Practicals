x=int(input("enter the number"))
n=int(input("enter the number of steps: "))
sum=0
for i in range(1,n+1):
    p=x**(i+1)
    sum=sum+(p/(i*2))
print(sum)