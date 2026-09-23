st=input("Enter a string: ")
#Set the counter value
ctr=0
ctr_a=0
ctr_i=0
ctr_o=0
ctr_u=0
ctr_e=0
#To find total number of vowels in string
for i in st:
    if i in 'aeiouAEIOU':
        ctr+=1
#To find number of individual vowels
for i in range(len(st)):
    #To find number of a
    if st[i]=='a':
        ctr_a+=1
    # To find number of i
    elif st[i]=='i':
        ctr_i+=1
    # To find number of o
    elif st[i]=='o':
        ctr_o+=1
    # To find number of u
    elif st[i]=='u':
        ctr_u+=1
    # To find number of e
    elif st[i]=='e':
        ctr_e+=1
print("Total number of vowels in",st,"is", ctr)
print("Total number of 'a' in",st,"is",ctr_a)
print("Total number of 'e' in",st,"is",ctr_e)
print("Total number of 'i' in",st,"is",ctr_i)
print("Total number of 'o' in",st,"is",ctr_o)
print("Total number of 'u' in",st,"is",ctr_u)
