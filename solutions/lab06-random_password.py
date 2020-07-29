

import string


def get_integer(text, min=0, max=99999):
    while True:
        num = input(text)
        if num.isdigit():
            num = int(num)
            if num < min or num > max:
                print('that is not a valid number')
                continue
            return num
        else:
            print('that is not a valid number')

def random_password(n_lowercase, n_uppercase, n_digits, n_punctuation):
    ...

    string.digits
    string.ascii_lowercase
    string.ascii_uppercase
    string.punctuation


print('Welcome the the random password generator 5000 (tm)')
n_lowercase = get_integer('how many lower case letters? ', 0, 100)
n_uppercase = get_integer('how many upper case letters? ')
n_digits = get_integer('how many digits? ')
n_punctuation = get_integer('how many punctuation characters?')






