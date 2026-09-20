#Number Guessing game
n=23
guess=1
print('Welcome to Number guessing game')
print('Number of guesses is limited to 9 times only')
while(guess<=9):
    num=int(input("Enter the number you guessed: "))
    if num>23:
        print('Please Enter a smaller number')
    elif num<23:
        print('Please enter a greater number')
    else:
        print('Congratulations! You won the game..')
        print('Number of guesses you took to win the game: ',guess)
        break
    print('Number of guesses left:', 9-guess)
    guess=guess+1
    if guess>9:
        print('You lost the game! Try Again next time!')
