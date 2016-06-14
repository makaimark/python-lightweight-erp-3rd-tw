# implement commonly used functions here

table = [["kH34Ju", "Age of Empires II: The Age of Kings", "Ensemble Studios", "32", "32"],
["jH34Ju", "Age of Mythology", "Ensemble Studios", "40", "4"],
["tH34Ju", "Age of Empires II: The Conquerors", "Ensemble Studios", "30", "3"]]

import random
import ui

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

result = generate_random(table)
print(result)


def common_add(table, title_list):
    new_id = [generate_random(table)]
    new_list = []
    new_add = ui.get_inputs("Give me an")
    for i in table:
        title_list[0] = title_list[i]
        new_list.append(ui.get_inputs("Give me an" + title_list))
        new_id.append(new_list[i])
    table.append(new_line)
    return table


def common_remove(table, id_):
    data_manager.get_table_from_file(file_name)
    data_manager.write_table_to_file(file_name)
    the_input = ui.get_inputs("Give me an ID: ")
    while True:
        for i in table:
            if i[0] == the_input:
                table.remove()
                break
            else:
                ui.print_error_message("This ID dosn't exist.")
                continu

common_remove()





# def common_update(table, title_list):
    # ui.get_inputs
