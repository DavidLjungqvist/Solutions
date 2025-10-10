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
        self.lenght = len(str(abs(value)))

    def __getitem__(self, index):
        return self.digits[index]

    def __add__(self, other):
        result = ""
        if self.lenght >= other.lenght:
            for digit in range(self.lenght):
                if digit >= other[digit]:
                    new_digit = digit
                else:
                    new_digit = self[digit]
                result += new_digit
        else:
            for digit in range(other.lenght):
                if digit >= self[digit]:
                    new_digit = digit
                else:
                    new_digit = other[digit]
                result += new_digit
        return result

    # def lunar_addition(self):

    # TRY TO PUT THE CODE IN A FUNCTION AND CALL THE FUNCTION UNDER __add__



    # def lunar_multiplication(self):

number1 = Lunar_int(120)
number2 = Lunar_int(315)

number3 = number1 + number2