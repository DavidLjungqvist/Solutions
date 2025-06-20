"""
Opgave "sequence1":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Skriv en funktion med navnet "sequence1".
Scroll ned for at finde det sted i denne fil, hvor du skal skrive funktionen ind.

Funktionen sequence1 skal ...
    have én parameter ved navn "max_value".
    udskrive alle heltal (integer) fra 1 op til og med maxvalue.

Eksempel: Når du kalder sequence1(3), printes 1 2 3.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


#  Write your function below this line:

# While loop solution:
def sequence1(max_value):
    number = 1
    while number <= max_value:
        print(number)
        number += 1

# For loop solution:
def sequence2(max_value):
    for i in range(max_value):
        print(i+1)

# Here starts the main program. Call your function here:

sequence1(5)
print("\n")
sequence2(5)