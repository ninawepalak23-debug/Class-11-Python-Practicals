n=int(input('Enter a number: '))
a,b=0,1
print('Fibonacci series upto first',n,'terms is: ')
print(a)
print(b)
for i in range(0,n-2):
    c=a+b
    a=b
    b=c
    print(c)