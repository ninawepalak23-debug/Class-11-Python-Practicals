#Start
print("Hello World")
#String Slicing
name = "harry is a good boy"
print(name[::-1])
#String functions
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.find("good"))
print(name.count("good"))
print(name.endswith("boy"))
print(name.endswith("harry"))
print(name.replace("harry", "Draco"))
#Lists
grocery = ["Flour","Soap","pizza","burger","cold drink",23]
print(grocery[1])
print(grocery[2])
print(grocery[3])
print(grocery[0])
numbers = [2,7,4,0,94,76]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))
#adding any number in list
numbers.append(10)
print(numbers)
#inserting number after any number in the list
numbers.insert(1,10)
print(numbers)
#removing any number from the list
numbers.remove(10)
print(numbers)
#removing number that is in the end of the list
numbers.pop()
print(numbers)