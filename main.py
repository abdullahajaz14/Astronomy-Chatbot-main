def getUserInput():
    i = input('Hello! \n')
    print(i)
    return i

def isQuestion(str):
    """Return True if the given string contains ?. It analyses if the user's input is a qustion or not."""
    return str.find('?') != -1

def findWord(str, word):
    return str.find(word) != -1

getUserInput()