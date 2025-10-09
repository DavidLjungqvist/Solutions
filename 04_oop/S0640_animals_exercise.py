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
        return (f"{self.name} is an {self.__class__.__name__} and says: {self.sound}. {"She's" if self.female else "He's"} {self.height}cm tall, weighs {self.weight}kg and has {self.legs} legs. "
                f"{self.name} also has a tail that's {self.tail_lenght}cm long and {"hunts" if self.hunts_sheep else "doesnt hunt"} sheep")

    def wag_tail(self):
        print(f"The {self.__class__.__name__} {self.name} wags it's {self.tail_lenght}cm tail")

    def mate(self, father, mother, name):
        child_name = name
        child_height = father


# class Creature:
#     def __init__(self, name, height, weight, sound, female, legs):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.sound = sound
#         self.female = female
#         self.legs = legs
#
    @classmethod
    def combine(cls, obj1, obj2):
        # Example logic to combine attributes:
        new_name = obj1.name + "-" + obj2.name
        new_height = (obj1.height + obj2.height) / 2
        new_weight = (obj1.weight + obj2.weight) / 2
        new_sound = obj1.sound  # take the first object's sound for instance
        new_female = obj1.female or obj2.female  # or some logic
        new_legs = max(obj1.legs, obj2.legs)

        # Create and return new combined object
        return cls(new_name, new_height, new_weight, new_sound, new_female, new_legs)
#
# # Usage:
# parent1 = Creature("Alpha", 180, 75, "Roar", True, 4)
# parent2 = Creature("Beta", 190, 85, "Growl", False, 4)
# child = Creature.combine(parent1, parent2)
# print(child.name, child.height, child.female)  # Alpha-Beta 185.0 True



dog1 = Dog("Sniffles", "woof", 30, 15, 4, False, 10, True)

dog1.make_noise()
dog1.wag_tail()


print(dog1)
