"""
Opgave "square numbers":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Skriv kode i funktionen, som printer alle kwadrattal (1, 4, 9, ...), som er mindre end limit.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""
import math


def print_squarenumbers1(limit):
    i = 1
    while i*i <= limit:
        print(i*i)
        i += 1


def print_squarenumbers2(limit):
    for i in range(1, math.ceil(limit**0.5)):
        print(i*i)


print_squarenumbers1(700)
print("\n")
print_squarenumbers2(700)
