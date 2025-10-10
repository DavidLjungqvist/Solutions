"""
Opgave "Animals"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Alt, hvad du har brug for at vide for at løse denne opgave, finder du i cars_oop-filerne.

Del 1:
    Definer en klasse ved navn Animal.
    Hvert objekt i denne klasse skal have attributterne name (str), sound (str), height (float),
    weight (float), legs (int), female (bool).
    I parentes står data typerne, dette attributterne typisk har.

Del 2:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Kald disse metoder for at oprette objekter af klassen Animal og for at udskrive dem i hovedprogrammet.

Del 3:
    Skriv en metode ved navn make_noise, som udskriver dyrets lyd i konsollen.
    Kald denne metode i hovedprogrammet.

Del 4:
    Definer en anden klasse Dog, som arver fra Animal.
    Hvert objekt af denne klasse skal have attributterne tail_length (int eller float)
    og hunts_sheep (typisk bool).

Del 5:
    Tilføj til klassen meningsfulde metoder __init__ og __repr__.
    Ved skrivning af konstruktoren for Dog skal du forsøge at genbruge kode fra klassen Animal.
    Kald disse metoder for at oprette objekter af klassen Hund og for at udskrive dem i hovedprogrammet.

Del 6:
    Kald metoden make_noise på Dog-objekter i hovedprogrammet.

Del 7:
    Skriv en metode ved navn wag_tail for Dog. Denne metode udskriver i konsollen noget i stil
    med "Hunden Snoopy vifter med sin 32 cm lange hale".
    Kald denne metode i hovedprogrammet.

Del 8:
    Skriv en funktion mate(mother, father) undenfor klassen. Begge parametre er af typen Dog.
    Denne funktion skal returnere et nyt objekt af typen Dog.
    I denne funktion skal du lave meningsfulde regler for den nye hunds attributter.
    Hvis du har lyst, brug random numbers så mate() producerer tilfældige hunde.
    Sørg for, at denne funktion kun accepterer hunde med det korrekte køn som argumenter.

Del 9:
    I hovedprogrammet kalder du denne metode og udskriver den nye hund.

Del 10:
    Gør det muligt at skrive puppy = daisy + brutus i stedet for puppy = mate(daisy, brutus)
    for at opnå den samme effekt.  Du bliver nok nødt til at google hvordan man laver det.

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""
import random


class Animal:
    def __init__(self, name: str, sound: str, height: float, weight: float, legs: int, female: bool):
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.legs = legs
        self.female = female

    def __repr__(self):
        return f"{self.name} is an {self.__class__.__name__} and says: {self.sound}. {"She's" if self.female else "He's"} {self.height}cm tall, weighs {self.weight}kg and has {self.legs} legs"

    def make_noise(self):
        print(f"{self.name} says {self.sound}")


class Dog(Animal):
    def __init__(self, name: str, sound: str, height: float, weight: float, legs: int, female: bool, tail_lenght: float, hunts_sheep: bool):
        super().__init__(name, sound, height, weight, legs, female)
        self.tail_lenght = tail_lenght
        self.hunts_sheep = hunts_sheep

    def __repr__(self):
        return (f"{self.name} is a {self.__class__.__name__} and says: {self.sound}. {"She's" if self.female else "He's"} {self.height}cm tall, weighs {self.weight}kg and has {self.legs} legs. "
                f"{self.name} also has a tail that's {self.tail_lenght}cm long and {"hunts" if self.hunts_sheep else "doesnt hunt"} sheep")

    def __add__(self, other):
        return mate(self, other, "Roses")

    def wag_tail(self):
        print(f"The {self.__class__.__name__} {self.name} wags it's {self.tail_lenght}cm tail")


def mate(father, mother, name: str):
    if father.female or not mother.female:  # Checks if genders are in the correct parameter slots
        return "Wrong genders, can't mate"  # Exits function if genders are incorrect
    child_name = name
    child_female = 0.5 > random.random()
    child_sound = mother.sound if child_female else father.sound  # Child takes the sound of the same gendered parrent
    child_height = (father.height + mother.height) / 2  # Child takes the average height of parents
    if not child_female:  # If the child is male it's taller
        child_height += 3
    child_weight = 9 + child_height // 5  # Calculates childs weight based on the height
    child_legs = 4
    if random.random() < 0.05:  # Small chance that the child is "mutated" and has an extra leg
        child_legs += 1
    child_tail_lenght = (father.tail_lenght + mother.tail_lenght) / 2  # Takes the average lenght of parents tail
    child_hunts_sheep = father.hunts_sheep or mother.hunts_sheep  # Child will hunt sheep if either of the parents also hunts sheep
    return Dog(child_name, child_sound, child_height, child_weight, child_legs, child_female, child_tail_lenght, child_hunts_sheep)


dog1 = Dog("Sniffles", "woof", 33, 16, 4, False, 10, True)
dog2 = Dog("Violet", "woofie", 25, 13, 4, True, 8, False)


dog1.make_noise()
dog1.wag_tail()


dog3 = mate(dog1, dog2, "Cupcake")
dog4 = dog1 + dog2

print(dog1)
print(dog2)
print(dog3)
print(dog4)
