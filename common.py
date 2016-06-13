# implement commonly used functions here

import random

table = ['h', 'k', 'hhh']
# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def generate_random(table):
    result = ""
    generated = ''
    i = 0

    while True:
        generated = generated + random.choice("abcdefghijklmnopqrstuvwxyz")
        generated = generated + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        generated = generated + random.choice("0123456789")
        generated = generated + random.choice("0123456789")
        generated = generated + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        generated = generated + random.choice("abcdefghijklmnopqrstuvwxyz")
        generated = generated + "#"
        generated = generated + "&"
        if generated in table:
            generated = ""
        else:
            return generated

result = generate_random(table)
print(result)
