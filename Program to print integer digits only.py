#Make a program that can print only integer digit from the list and the item should be greater than 6.
# noinspection SpellCheckingInspection
list1=['Palak','Iron man', 8,9,2,7]
for item in list1:
    if type(item)==int and item>6:
        print(item)