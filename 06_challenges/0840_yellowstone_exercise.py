"""Opgave "Yellowstone"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.


Skriv en funktion som beregner Yellowstone-følgen. For at nå det, løs de følgende delopgaver:

Del 1:
    Se de første 4 minutter og 16 sekunder af denne video:
    https://www.youtube.com/watch?v=DUaqiM1bGX4

    Hvis du hellere vil have reglerne på skrift:
    Definer en række positive heltal ved hjælp af reglerne, at
        a(1) = 1, a(2) = 2, a(3) = 3,
        og for n ≥ 4 er a(n) det mindste tal, der ikke allerede er i rækken,
        som har en fælles faktor med a(n - 2), men som er relativt primtal i forhold til a(n - 1).
Del 2:
    Skriv en funktion prime_list(n), der returnerer de første n primtal som en list.

Del 3:
    Skriv en funktion prime_factorization(number), der returnerer
    en list over primfaktorerne for number.

    Prime factorization eller integer factorization af et tal er at nedbryde et
    tal til et sæt af primtal, som ganges sammen for at resultere i det oprindelige tal.
    Dette er også kendt som prime decomposition.
    Eksempel: 2, 2, 5 er primfaktoriseringen af 20.

Del 4:
    Skriv en funktion greatest_common_divisor(number1, number2), der returnerer den største fælles divisor for de to tal.
    Eksempel: Den største fælles divisor for 20 og 70 er 10 (fordi 20 og 70 har de fælles primfaktorer 2 og 5).

Del 5:
    Skriv en funktion relative_prime(number1, number2), der returnerer True, hvis de to tal er relative primtal
    til hinanden, ellers False.
    Relativt primtal betyder, at den største fælles divisor for de to tal er 1.

Del 6:
    Skriv en funktion yellowstone(n), der returnerer de første n elementer af Yellowstone-følgen som en list.
    Brug denne liste til at kontrollere din løsning: https://oeis.org/A098550/b098550.txt

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

def common_divider(first_factors, second_factors):
    return bool(first_factors.intersection(second_factors))

def no_common_terms(first_factors, second_factors):
    boolean = bool(first_factors.intersection(second_factors))
    return not boolean


def find_prime_factors(number):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    factors_of_number = []
    current_calculation = number
    while current_calculation != 1:
        for i in prime_numbers:
            if current_calculation % i == 0:
                current_calculation /= i
                factors_of_number.append(i)
                break
    unique_factors_of_number = set(factors_of_number)
    return unique_factors_of_number


def calculate_factor_conditions(new_num, yellowstone_sequence):
    unique_factors_new_number = find_prime_factors(new_num)
    unique_factors_yellowstone_last = find_prime_factors(yellowstone_sequence[-1])
    unique_factors_yellowstone_second_last = find_prime_factors(yellowstone_sequence[-2])
    no_common_terms_bool = no_common_terms(unique_factors_new_number, unique_factors_yellowstone_last)
    common_divider_bool = common_divider(unique_factors_new_number, unique_factors_yellowstone_second_last)
    if no_common_terms_bool and common_divider_bool:
        return True
    else:
        return False


def new_number(yellowstone_sequence):
    for new_num in range(1, 1000):
        if new_num not in yellowstone_sequence:
            if calculate_factor_conditions(new_num, yellowstone_sequence):
                yellowstone_sequence.append(new_num)
                break
    return yellowstone_sequence


def main(sequence_lenght: int, yellowstone_sequence: list):
    for i in range(sequence_lenght):
        yellowstone_sequence = new_number(yellowstone_sequence)
    print(yellowstone_sequence)


main(40, [1, 2, 3])
