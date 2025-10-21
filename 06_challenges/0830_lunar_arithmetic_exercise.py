"""Opgave "Lunar arithmetic"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=cZkGeR9CWbk

Del 2:
    Skriv en klasse Lunar_int(), med metoder, der gør, at du kan anvende operatorerne + og * på
    objekter af denne klasse, og at resultaterne svarer til de regler, der forklares i videoen.

Del 3:
    Se resten af videoen.

Del 4:
    Skriv en funktion calc_lunar_primes(n), som retunerer en liste med de første n lunar primes.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""


class Lunar_int():
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return (self.value)

    def __add__(self, other):
        return Lunar_int(lunar_addition(self, other))

        # result = ""
        # if self.lenght >= other.lenght:
        #     for digit in range(self.lenght):
        #         if digit >= other[digit]:
        #             new_digit = digit
        #         else:
        #             new_digit = self[digit]
        #         result += new_digit
        # else:
        #     for digit in range(other.lenght):
        #         if digit >= self[digit]:
        #             new_digit = digit
        #         else:
        #             new_digit = other[digit]
        #         result += new_digit
        # return result


def lunar_addition(self, other):
    # first_list = []
    # second_list = []
    result = []
    # for number in range(self):  # Runs through the first number and appends each digit into "first_list"
    #     first_list.append(number)
    # for number in range(other):  # Runs through the second number and append each digit into "second_list"
    #     second_list.append(number)
    first_list = [int(d) for d in str(self.value)]
    second_list = [int(d) for d in str(other.value)]
    if len(first_list) >= len(second_list):  # Compares list lenghts and uses the greater lenght list as a reference
        longer_number, shorter_number = first_list, second_list
    else:
        longer_number, shorter_number = second_list, first_list
    for i, j in zip(shorter_number, longer_number):
        max_value = max(i, j)
        result.append(max_value)
        print(i)
        print(j)
    # for i in range(len(longer_number) - 1, (len(longer_number) - len(shorter_number)) - 1, -1):
    #         max_value = max(longer_number[i], shorter_number[i])
    #         result.append(max_value)

    print(result)
    # return Lunar_int(result)

#  The zip should end and the remaining numbers in the list have to merged to the result


    # def lunar_multiplication(self):

number1 = Lunar_int(120)
number2 = Lunar_int(315)

number3 = number1 + number2
# print(number3)