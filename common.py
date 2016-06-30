# implement commonly used functions here

import random
import ui
import data_manager


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)


def generate_random(table):
    result = ""
    generated = ""

    while True:
        for i in range(0, 2):
            generated = generated + random.choice("abcdefghijklmnopqrstuvwxyz")
            generated = generated + random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            generated = generated + random.choice("0123456789")
            generated = generated + random.choice("<>#&@{}<")
        ''.join(random.sample(generated, len(generated)))
        if generated in table:
            generated = ""
        else:
            return generated


def common_add(table, title_list):
    new_add = []
    new_id = generate_random(table)
    new_add = ui.get_inputs(title_list, "Give me an")
    new_add.insert(0, new_id)
    table.append(new_add)
    return table


def common_remove(table, id_):
    for i in table:
        if i[0] == id_:
            table.remove(i)
            return table
    ui.print_error_message("This ID doesn't exist.")
    return table


def common_update(table, title_list, id_):
    new_line = []
    new_line.append(id_)
    new_line += ui.get_inputs(title_list, "Update the information")
    for i in table:
        if i[0] == id_:
            table.remove(i)
            table.append(new_line)
            return table
    ui.print_error_message("This ID doesn't exist.")
    return table
