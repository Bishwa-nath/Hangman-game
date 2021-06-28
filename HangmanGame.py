# Hangman game
# ----------------------------------

import random
import string

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


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for s in secretWord:
        if s not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''
    for l in secretWord:
        if l in lettersGuessed:
            s += l
        else:
            s += '_ '
    return s


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s = string.ascii_lowercase

    for i in lettersGuessed:
        if i in s:
            s = s.replace(i, "")
    return s


def update(i, x):
    # Shows messages what to do.
    print("-------------")
    print("You have", i, "guesses left.")
    print("Available letters:", x)
    print("Please guess a letter: ", end="")


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
    '''
    print("Welcome to the game Hangman!")
    length = len(secretWord)
    print("I am thinking of a word that is", length, " letters long.")
    i = 8
    letters = []
    x = getAvailableLetters(letters)
    testWord = ""
    testWord2 = ""
    update(i, x)

    while True:
        letter = input()
        letters += letter
        x = getAvailableLetters(letters)

        if letter in secretWord or letter in testWord:
            if letter in testWord:
                print("Oops! You've already guessed that letter:", testWord)
            else:
                word = getGuessedWord(secretWord, letters)
                print("Good guess:", word)
                testWord = word
                if isWordGuessed(secretWord, letters):
                    print("-----------")
                    print("Congratulations, you won!")
                    break
            if i != 0:
                update(i, x)

        elif letter not in secretWord or letter in testWord2:
            if letter in testWord2:
                print("Oops! You've already guessed that letter:", testWord)
            else:
                word = getGuessedWord(secretWord, letters)
                print("Oops! That letter is not in my word:", word)
                testWord = word
                testWord2 += letter
                i -= 1
            if i != 0:
                update(i, x)

        if i == 0:
            print("-----------")
            print("Sorry, you ran out of guesses. The word was", secretWord+".")
            break


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
