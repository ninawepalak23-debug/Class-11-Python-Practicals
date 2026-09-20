n=int(input('Enter a number: '))
sum=0
for i in range(len(str(n))):
    digit=n%10
    sum=sum+digit
    n=n//10
print('Sum of digits is: ',sum)