"""
Kør dette program.
Tilføj oop-relaterede kommentarer til denne kode.
    Eksempler:
        class definition / klasse definition
        constructor / konstruktor
        inheritance / nedarvning
        object definition / objekt definition
        attribute / attribut
        method / metode
        polymorphism / polymorfisme
        encapsulation: protected attribute / indkapsling: beskyttet attribut
        encapsulation: protected method / indkapsling: beskyttet metode
"""


class Building: # Dette definerer er en klasse
    def __init__(self, area, floors, value): # Dette er kontruktoren
        self.area = area # Disse linjer er atributer af de objekter der bliver lavet med klassen "Building"
        self.floors = floors
        self._value = value

    def renovate(self): # Metode - funktion i en klasse
        print("Installing an extra bathroom...")
        self._adjust_value(10) # Polymorfisme

    def _adjust_value(self, percentage): # Enkapsling: beskyttet metode
        self._value *= 1 + (percentage / 100) # Enkapsling: beskyttet atribut
        print(f'Value has been adjusted by {percentage}% to {self._value:.2f}\n')


class Skyscraper(Building): # Her er der nedarvning fra klassen "Building"

    def renovate(self):
        print("Installing a faster elevator.")
        self._adjust_value(6) # Polymorfisme


small_house = Building(160, 2, 200000) # Objekt definition
skyscraper = Skyscraper(5000, 25, 10000000)

for building in [small_house, skyscraper]:
    print(f'This building has {building.floors} floors and an area of {building.area} square meters.')
    building.renovate()
