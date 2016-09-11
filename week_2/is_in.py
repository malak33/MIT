def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
#    if b == 0:
#       return a
#    else:
#       return gcdRecur(b, a % b)
    if len(aStr) == 0 or (len(aStr) == 1 and char.toString != aStr):
        return False
    elif aStr[len(aStr) // 2] == char:
        return True
    elif aStr[len(aStr) // 2] > char:
        return isIn(char, aStr[:len(aStr) // 2])
    else:
        return isIn(char, aStr[len(aStr) // 2 + 1:])
