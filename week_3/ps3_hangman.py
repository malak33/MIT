# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    #sWord = secretWord
    count = 0
    for i in secretWord:
        if i in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    blank = ['_ '] * len(secretWord)

    for i, c in enumerate(secretWord):
        if c in lettersGuessed:
            count += 1
            blank.insert(count-1,c)
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)
        else:
            count += 1
            blank.insert(count-1,'_')
            blank.pop(count)
            if count == len(secretWord):
                return ''.join(str(e) for e in blank)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    letters2 = letters1
    count = 0
    while count <= 52:
        for lett in lettersGuessed:
            if lett in letters2:
                letters2.remove(lett)
                count += 1
                #print(letters2)
        #print(letters2.strip)
        return ''.join(letters2)


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



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)


# print(hangman(c))
