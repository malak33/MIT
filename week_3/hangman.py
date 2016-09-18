def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...


    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 8
    wordGuessed = False

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + intro + ' letters long.')
    print('------------')

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print('You have ' + str(mistakesMade) + ' guesses left.')
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print('------------')
            else:
                lettersGuessed.append(guess)
                print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
                print('------------')
        else:
            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
                print('------------')

    if wordGuessed == True:
        return 'Congratulations, you won!'
    elif mistakesMade == 0:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)