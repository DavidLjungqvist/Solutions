"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


class Miner:
    def __init__(self):
        self.sleepiness = 0
        self.thirst = 0
        self.hunger = 0
        self.whisky = 0
        self.gold = 0
        self.turn = 0

    def sleep(self):
        self.sleepiness -= 10
        self.thirst += 1
        self.hunger += 1

    def mine(self):
        self.sleepiness += 5
        self.thirst += 5
        self.hunger += 5
        self.gold += 5

    def eat(self):
        self.sleepiness += 5
        self.thirst -= 5
        self.hunger -= 20
        self.gold -= 2

    def buy_whisky(self):
        self.sleepiness += 5
        self.thirst += 1
        self.hunger += 1
        self.whisky += 1
        self.gold -= 1

    def drink(self):
        self.sleepiness += 5
        self.thirst -= 15
        self.hunger -= 1
        self.whisky -= 1


morris = Miner()

def dead():
    return (morris.sleepiness> 100 or morris.thirst> 100 or morris.hunger > 100)

while not dead() and morris.turn < 1000:
    morris.turn += 1
    if morris.sleepiness > 90:
        morris.sleep()
    elif morris.thirst >= 95 and morris.whisky > 0:
        morris.drink()
    elif morris.thirst >= 90 and morris.whisky == 0:
        morris.buy_whisky()
    elif morris.hunger > 90:
        morris.eat()
    else:
        morris.mine()
    print(f"Turn:{morris.turn} Sleepiness:{morris.sleepiness} Thist:{morris.thirst} Hunger:{morris.hunger} Whisky:{morris.whisky} Gold:{morris.gold}")

