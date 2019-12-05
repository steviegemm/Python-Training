# P77 - more for loops

# Lists such as  rabbits are one of Python’s iterable objects, along with strings, tuples,
# dictionaries, sets, and some other elements. Tuple or list iteration produces an item at
# a time. String iteration produces a character at a time, as shown here:

word = 'cat'
for letter in word:
    print(letter)
    
# Iterating over a dictionary (or its  keys() function) returns the keys. In this example,
# the keys are the types of cards in the board game Clue (Cluedo outside of North America):
accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
for card in accusation: # or, for card in accusation.keys():
    print(card)
    
# To iterate over the values rather than the keys, you use the dictionary’s  values() function:
for value in accusation.values():
    print(value)
    
# To return both the key and value in a tuple, you can use the  items() function:
for item in accusation.items():
    print(item)  

# Remember that you can assign to a tuple in one step. For each tuple returned by
# items() , assign the first value (the key) to  card and the second (the value) to  contents :
for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)
    

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else: # no break means no cheese
    print('This is not much of a cheese shop, is it?')