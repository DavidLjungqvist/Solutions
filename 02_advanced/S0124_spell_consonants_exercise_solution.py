"""
Opgave "spell_consonants":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Forandre koden i funktionen spell_consonants() sådan at den gør hvad der står i dens dokumentation.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


def spell_consonants(text, letter_limit):
    for letter in text:
        if letter.lower() in letter_limit:
            pass
        else:
            print(letter, end=" ")
    print()


    """
    Spells/prints the first letter_limit letters of text.
    Prints only consonants and spaces (a, e, i, o, u, y do not get printed). """
    pass


spell_consonants("Hello world", letter_limit=["a", "e", "i", "o", "u", "y"])  # should print "Hll wr"
spell_consonants("I love Python", letter_limit=["a", "e", "i", "o", "u", "y"])  # should print "I lv Pt"
