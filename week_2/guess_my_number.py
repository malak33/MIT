high = 0
low = 0
guess = 50
new_guess = 0
num_guesses = 100
x = ''
h = ''
l = ''
c = ''

# def main():
print('Please think of a number between 0 and 100!')
while num_guesses > 1:

    print('Is your secret number {} ?'.format(guess))
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
            "Enter 'c' to indicate I guessed correctly. ")
#    if x != h or c or l:
#        print('Sorry, I did not understand your input.')
#        num_guesses -= 1

    if x == 'c':
        print('Game over. Your secret number was: {}'.format(guess))
        print('pressed c')
        num_guesses -= 1

    elif x == 'h':     # they pressed h
        new_guess = guess / 2.0
        print(new_guess)
        print('pressed h')
        num_guesses -= 1
    elif x == 'l':   # they pressed l
        new_guess = guess * 2.0
        print(new_guess)
        print('pressed l')
        num_guesses -= 1
    else:

        num_guesses -= 1
#elif x == l:
#    pass
#elif x == c:
#    print('Game over. Your secret number was: ' + guess)
#else:
#    print('Sorry, I did not understand your input.')






#    if __name__ == '__main__':
#        main()