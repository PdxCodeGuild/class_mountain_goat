

import random


def get_value(value):
    if value == 'A':
        return 1
    elif value in ['J', 'Q', 'K']:
        return 10
    else:
        return int(value)



suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

# print(len(suites)*len(values))

deck = []
for suit in suits:
    for value in values:
        # deck.append((value, suit)) # append a tuple to the list
        deck.append({
            'suit': suit,
            'value': value,
            'letter_value': value[0],
            'numerical_value': get_value(value[0])
        })

random.shuffle(deck)

card = deck.pop(random.randint(0, len(deck)-1))
print('You got ' + card['value'] + ' of ' + card['suit'])
