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
        return self.value

    def __add__(self, other):
        return Lunar_int(lunar_addition(self, other))

    def __mul__(self, other):
        return Lunar_int(lunar_multiplication(self, other))

def lunar_addition(self, other):
    result = []
    first_list = [int(d) for d in str(self.value)]
    second_list = [int(d) for d in str(other.value)]
    if len(first_list) >= len(second_list):  # Compares list lenghts and uses the greater lenght list as a reference
        longer_number, shorter_number = first_list, second_list
    else:
        longer_number, shorter_number = second_list, first_list
    first_digits = []
    digit_difference = len(longer_number) - len(shorter_number)
    for digit in range(digit_difference):
        first_digits.append(longer_number[digit])
    for digit in range(digit_difference):
        longer_number.pop(1)
    for i in first_digits:
        result.append(i)
    for i, j in zip(shorter_number, longer_number):
        max_value = max(i, j)
        result.append(max_value)
    return list_to_integer(result)


def list_to_integer(list_of_ints):
    return int(''.join(map(str, list_of_ints)))


def lunar_multiplication(self, other):
    result_list = []
    first_list = [int(d) for d in str(self.value)]
    second_list = [int(d) for d in str(other.value)]
    reversed_first_list = list(reversed(first_list))
    reversed_second_list = list(reversed(second_list))
    for i, num1 in enumerate(reversed_first_list):
        result = [0] * i
        for num2 in reversed_second_list:
            min_num = min(num1, num2)
            result.append(min_num)
        result_list.append(result)
    reversed_result_list = []
    for i in range(len(result_list)):
        # reversed_result_list.append(list(reversed(result_list[i])))
        current_list = result_list[i]
        reversed_list = list(reversed(current_list))
        reversed_result_list.append(reversed_list)
    result = []
    for items in zip(*result_list):
        result.append(max(items))
    print(result)

def multiply_part_two():
    # result_list
    result_list = [[1, 3, 5], [0, 2, 4, 6, 8], [3, 5, 7, 9]]
    for i in result_list:
        new_list = []
        for j in result_list[i]:
            new_list.append(j)
        min_num = min(new_list)


# number1 = Lunar_int(  820)
# number2 = Lunar_int(12315)
# number3 = number1 + number2
# print(number3.value)


number4 = Lunar_int( 43)
number5 = Lunar_int(136)
number6 = number4 * number5