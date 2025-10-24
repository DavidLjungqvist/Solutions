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
        print(i)
        print(j)
    print(result)

def lunar_multiplication(self, other):


number1 = Lunar_int(820)
number2 = Lunar_int(12315)
number3 = number1 + number2