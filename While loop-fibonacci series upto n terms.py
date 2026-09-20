n=int(input('Enter a number: '))
a,b=0,1
print('Fibonacci series upto first',n,'terms is: ')
print(a)
print(b)
i=0
while i>=0 and i<n-2:
    c=a+b
    a=b
    b=c
    print(c)
    i=i+1