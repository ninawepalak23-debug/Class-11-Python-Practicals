#Create a dictionary and take input from user and return the meaning of the word from dictionary
d1 = {'Upward':'going up','Downward':'going down','AI':'Artificial Intelligence-it is the ability of machines to mimic human intelligence'}
list1 = ['Upward','Downward','AI']
print("Here is the list of words of which you can find meaning: ", list1)
print(d1.get(input("Enter a word:")))