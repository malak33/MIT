animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    # return max(animals, key=animals.get)
    return max(animals.values())

print(biggest(animals))
print(biggest({'b': [1, 7, 5, 4, 3, 18, 10, 0], 'a': []}))