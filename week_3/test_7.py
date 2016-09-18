animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    #return len(aDict.values())
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result

    """
    myDict = {}
    for word in aDict:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return len(myDict)
    """


print(how_many(animals))
print(how_many({'u': [10, 15, 5, 2, 6], 'B': [15]}))