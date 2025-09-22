"""Opgave "Number pyramid"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Del 2:
    Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
    Funktionen har en parameter "lines", der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række og også deres sum.

Del 3:
    I hovedprogrammet kalder du funktionen med fx 7 som argument.

Del 4:
    Tilføj en mere generel funktion pyramid2.
    Denne funktion har som andet parameter "firstline" en liste med pyramidens øverste rækkens tallene.

Del 5:
    I hovedprogrammet kalder du pyramid2 med fx 10 som det første argument
    og en liste med tal efter eget valg som andet argument.
    Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne 0812_pyramid_help.py og starte derfra

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


# def pyramid(pyramid_height: int, firstline: list):
#     my_list = firstline
#     current_line = 1
#     for j in range(pyramid_height):
#         print(my_list)
#         current_line += 1
#         new_list = my_list
#         new_list_offset = 1
#         for i in range(len(my_list)):
#             left = my_list[i-1] if i - 1 >=  0 else 0
#             right = my_list[i+1] if i + 1 < len(my_list) else 0
#             print(left + my_list[i] + right)
#             if left + my_list[i] + right == current_line and my_list[i] != len(my_list):
#                 new_list.insert(i + new_list_offset, left + my_list[i] + right)
#                 new_list_offset += 1
#             elif left + my_list[i] + right == current_line and my_list[i] == len(my_list):
#                 new_list.insert(i + new_list_offset - 1, left + my_list[i] + right)


def pyramid(lines: int, firstline: list):
    current_line_digits = firstline
    current_line = 1
    for j in range(lines):
        print(current_line_digits)
        current_line += 1
        new_line_digits = []
        for i in range(len(current_line_digits) - 1):
            new_line_digits.append(current_line_digits[i])
            if current_line_digits[i] + current_line_digits[i + 1] == current_line:
                new_line_digits.append(current_line_digits[i] + current_line_digits[i + 1])
        new_line_digits.append(current_line_digits[-1])
        current_line_digits = new_line_digits.copy()


pyramid(10, [1, 1])
