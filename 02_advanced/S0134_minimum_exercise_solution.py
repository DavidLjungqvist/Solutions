"""
Opgave "minimum":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Skriv en funktion med navnet "minimum".

Funktionen minimum skal ...
    have én parameter ved navn "numberlist".
    ikke bruge pythons inbyggede funktion min.
    returnere den mindste tal som er i numberlist.
    blive kaldt med en liste som argument.

Der er allerede kodelinjer i hovedprogrammet, der kalder denne funktion.

Kør programmet. Først 2 og derefter 1 bør udskrives i konsollen. Får du de rigtige resultater?

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""
def minimum(numberlist):
    lowest_number = numberlist[0]
    for i in numberlist:
        if lowest_number > i:
            lowest_number = i
        else:
            continue
    return lowest_number


print(minimum([6, 2, 7, 3]))  # Should print 2
print(minimum([8, 17, 8, 3, 5, 1, 3]))  # Should print 1
