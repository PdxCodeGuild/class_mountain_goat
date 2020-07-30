# Return the number of letter occurances in a string.

def count_letter(letter, word):
    letter_count = 0
    for char in word:
        if char == letter:
            letter_count += 1
    return letter_count

# print(count_letter('i', 'antidisestablishmentterianism')) # 5
# print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')) # 2



# print(ord('a')) # 97
# print(ord('b')) # 98
# print(chr(97)) # 'a'

# #      01234
# print('hello'.index('o')) # 4


# Return the letter that appears the latest in the english alphabet.

def latest_letter(word):
    base = 97 
    for char in word:
        base = max(base, ord(char))
        #print(char, ord(char))
    base = chr(base)
    return base

    # word = list(word)
    # word.sort()
    # # return word[-1]
    # return word[len(word)-1]

    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # running_max = 0
    # for char in word:
    #     index = alphabet.index(char)
    #     # print(char, index)
    #     # running_max = max(running_max, index)
    #     if index > running_max:
    #         running_max = index
    # return alphabet[running_max]

# print(latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')) # v


# Write a function that returns the number of occurances of 'hi' in a given string.


# print('hello world world world'.find('world')) # 6
# print('hello world world world'.find('world', 7)) # 12
# print('hello world world world'.find('world', 13)) # 18
# print('hello world world world'.find('world', 19)) # 18

import re

def count_hi(text):
    # return text.count('hi')

    # count = 0
    # starting_index = 0
    # while True:
    #     index = text.find('hi', starting_index)
    #     if index == -1:
    #         break
    #     count += 1
    #     starting_index = index + 1
    # return count

    # results = re.findall('hi', text)
    # return len(results)




    count = 0
    for i in range(len(text)-1):
        # print(len(text), i, i+1)
        # text[i+1]
        if text[i] == 'h' and text[i+1] == 'i':
            count += 1
    return count






#               0123
print(count_hi('hihih')) # 2
print(count_hi('hello23hi45world hi 123abcllamama hi')) # 3



# falsey values: 0, '', [], {}, None, False
# everything else is truthy


# values = [0, 1, '', 'hi', [], ['hi'], {}, {'a':1}]
# for value in values:
#     print(value, 'is', end=' ')
#     if value:
#         print('truthy')
#     else:
#         print('falsey')




