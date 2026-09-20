# n = int(input("Enter the number: "))
# for i in range(0,n):
#     for j in range(0,n):
#         if i==0 or j==0 or i==n-1 or j==n-1:
#             print("*", end="    ")
#         else:
#             print(" ", end="    ")
#     print()


for i in range(0,7):
    for j in range(0,7):
        if i==0 or j==0 or i==6 or j==6:
            print("#", end="    ")
        else:
            print("  ", end="    ")
    print()