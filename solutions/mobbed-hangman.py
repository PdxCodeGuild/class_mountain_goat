



with open('english.txt') as file:
    text = file.read()
words = text.split()
words = [word for word in words if len(word) >= 5]
words.sort()
with open('english.txt', 'w') as file:
    file.write('\n'.join(words))