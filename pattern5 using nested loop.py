n=int(input("Enter a number: "))
for i in range(n,0,-1):
    for j in range(1,i):
        print(j, end="     ")
    print(i)