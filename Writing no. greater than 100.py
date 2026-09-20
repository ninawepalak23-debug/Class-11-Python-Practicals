#Make a program that takes input from the user until the number entered is greater than 100.
while True:
    inp=int(input('Enter a Number: '))
    if inp>100:
        print('Congratulations! You entered a number greater than 100..')
        break
    else:
        print('Try Again')
        continue