"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=rBU9E-ZOZAI

Del 2:
    Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
    Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række.

    Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
    et bestemt antal optræder i den aktuelle talrække.

Del 3:
    I hovedprogrammet kalder du inventory() med fx 6 som argument.

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du kigge på løsningen
i 0822_inventory_solution.py

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
# from collections import Counter


# def inventory(number_of_rows: int):
#     current_inventory = [1, 3, 4, 5, 1, 2, 3, 0]
#     for n in range(max(current_inventory)):
#
#     counter = {}
#     for number in current_inventory:
#         counter[number] = counter.get(number, 0) + 1
#
#     dict_sorted_by_keys = {key: counter[key] for key in sorted(counter)}
#
#     print(min(current_inventory))
#
#     print(dict_sorted_by_keys)


    # list_of_dicts = []


    # lines.append({'0': 0})
    # lines.append({'0': 1, '1': 1, '2': 0})
    # lines.append({'0': 2, '1': 2, '2': 2, '3': 0})





count_dict = {'0': 0, '1': 0, '2': 0, '3': 0}

# def count_number(number):
#     for line in lines:
#         for key in line:
#             if line[key] == number:
#                 count_dict[key] += 1





    # for m in range(my_dict):



# for l in range(len(lines)):
#     n = 0
#     entry = {}
#     while True:
#         # entry[f"{n}'s"] = list(my_dict.values()).count(n)
#         count = list(lines[l].values()).count(n)
#
#
#         if count == 0:
#             break
#
#         entry[f"{n}'s"] = count
#         n += 1

#    print(entry)




    # another_dict = {}
    # for n in range(number_of_rows):
    #     # my_dictionary[n] = {f"{}" : n}
    #
    #
    #
    #     another_dict[f"{n}'s"] = 1




    # value_counts = Counter(my_dict.values())
    # dict_sorted_by_keys = {key: value_counts[key] for key in sorted(value_counts)}

# inventory()

# def inventory(rows):
#     my_list = []
#     for r in range(rows):
#     current_line_dictionary = {
#         f"{nummeral}'s" :
#     }




def count_number(number, current_line, lines):
    number_amount = 0
    for line in lines:
        for value in line.values():
            if value == number:
                number_amount += 1
    for value in current_line.values():
        if value == number:
            number_amount += 1
    return number_amount


def count_lines(lines):
    n = 0
    new_dict = {}
    while True:
        number_amount = count_number(n, new_dict, lines)
        new_dict[n] = number_amount
        n += 1
        if number_amount == 0:
            lines.append(new_dict)
            return lines


def main(number_of_lines):
    lines = []
    for n in range(number_of_lines):
        lines = count_lines(lines)
    for i in lines:
        print(i)


main(16)
