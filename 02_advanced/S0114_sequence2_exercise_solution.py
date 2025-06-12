"""
Opgave "sequence2":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Skriv en funktion med navnet "sequence2".
Scroll ned for at finde det sted i denne fil, hvor du skal skrive funktionen ind.

Del 1:
    Funktionen sequence2 skal have to parameter: "min_value" og "max_value".
    Funktionen skal udskrive heltal fra min_value op til og med maxvalue.

    Eksempel: Når du kalder sequence2(3, 5), printes 3 4 5.


Del 2:
    Dupliker hele funktionskoden. (Du kan med fordel marker hele
    funktionen og derefter taste CTRL+D.)
    Kald funktionen i duplikatet sequence3.
    Tilføj en tredje parameter "step_size" til sequence3.
    Funktionen skal udskrive heltal fra min_value op til og med maxvalue.
    Den skal dog ikke udskrive hver tal. Der skal være et mellemrum med
    størrelsen step_size mellem de udskrevne tal.

    Eksempel: Når du kalder sequence3(3, 18, 4), printes 3 7 11 15.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


#  Write your function below this line:

# Del 1:

# While loop solution:
def sequence1(min_value, max_value):
    number = min_value
    while number <= max_value:
        print(number)
        number += 1


# For loop solution:
def sequence2(min_value, max_value):
    for i in range(min_value, max_value+1):
        print(i)


# Del 2:

# While loop solution:
def sequence3(min_value, max_value, step_size):
    number = min_value
    while number <= max_value:
        print(number)
        number += step_size


# For loop solution:
def sequence4(min_value, max_value, step_size):
    for i in range(min_value, max_value+1, step_size):
        print(i)


# Here starts the main program. Call your function here:

# Del 1:

sequence1(1, 5)     # While loop
print("\n")
sequence2(1, 5)     # For loop

print("\n####### Del 2 #######\n")
# Del 2:

sequence3(3, 18, 4)     # While loop
print("\n")
sequence4(3, 18, 4)     # For loop
