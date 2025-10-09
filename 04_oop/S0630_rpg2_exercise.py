"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import random

competition_lenght = 100

class Character:
    def __init__(self, name: str, ad: int, max_hp: int):
        self.name = name
        self.ad = ad
        self.max_hp = max_hp
        self._current_hp = max_hp
        self.is_stunned = False
        self.is_cursed = False
        self.is_alive = True
        self.score = 0

    def __repr__(self):
        return f"Character name is {self.name}. Max health: {self.max_hp}. Current health {self._current_hp}. Attackpower: {self.ad}."

    def default_attack(self, other):
        self.hit(other)

    def respawn(self):
        self._current_hp = self.max_hp
        self.is_stunned = False
        self.is_cursed = False
        self.is_alive = True

    def hit(self, target):
        print(f"{self.name} hits {target.name} for {self.ad} damage")
        target.get_hit(self.ad)

    def get_hit(self, attackpower):
        self._current_hp -= attackpower
        if self._current_hp <= 0:
            self.is_alive = False
            print(f"{self.name} has died")
        self.is_cursed = False
        self.is_stunned = False

    def get_healed(self, healpower):
        self._current_hp += healpower
        if self._current_hp > self.max_hp:
            self._current_hp = self.max_hp

    def get_crippling_shot(self, attackpower):
        self._current_hp -= attackpower
        self.is_stunned = True
        if self._current_hp <= 0:
            self.is_alive = False
            print(f"{self.name} has died")

    def get_cursed(self, ):
        self.is_cursed = True

class Healer(Character):
    def __init__(self, name: str, ad: int, max_hp: int, heal_pwr: int):
        super().__init__(name, ad, max_hp)
        self.heal_pwr = heal_pwr

    def heal(self, target):
        target.get_healed(self.heal_pwr)

class Hunter(Character):
    def __init__(self, name: str, ad: int, max_hp: int, perception: int):
        super().__init__(name, ad, max_hp)
        self.perception = perception

    def __repr__(self):
        return f"{self.name}: Max health: {self.max_hp}. Current health {self._current_hp}. Attackpower: {self.ad}. Perception: {self.perception}"

    def default_attack(self, other):
        if other.is_stunned or random.random() > 1 / 4:
            self.hit(other)
        else:
            self.crippling_shot(other)

    def crippling_shot(self, target):
        if self.perception * 0.1 + random.random() > 1:
            target.get_crippling_shot(self.ad)
            print(f"{self.name} cripples {target.name}")
        else:
            print(f"{self.name} misses a crippeling shot on {target.name}")

class Magician(Character):
    def __init__(self, name: str, atc: int, max_hp: int, spell_pwr: int):
        super().__init__(name, atc, max_hp)
        self.spell_pwr = spell_pwr

    def __repr__(self):
        return f"{self.name}: Max health: {self.max_hp}. Current health {self._current_hp}. Attackpower: {self.ad}. Spell power: {self.spell_pwr}"

    def hit(self, target):
        if target.is_cursed:
            print(f"{self.name} hits {target.name} for {self.ad * self.spell_pwr} damage")
            target.get_hit(self.ad * self.spell_pwr)
        else:
            print(f"{self.name} hits {target.name} for {self.ad} damage")
            target.get_hit(self.ad)

    def cast_curse(self, target):
        if random.random() > 0.5:
            target.get_cursed()
            print(f"{self.name} casts a curse on {target.name}")
        else:
            print(f"{self.name} misses a curse on {target.name}")

    def default_attack(self, other):
        if other.is_alive and not self.is_stunned:
            if self.is_cursed or random.random() > 1 / 4:
                self.hit(other)
            else:
                self.cast_curse(other)

def battle_simulator(rpg1, rpg2):
    for battle in range(competition_lenght):
        rpg1.respawn()
        rpg2.respawn()
        while rpg1.is_alive and rpg2.is_alive:
            # player1(rpg1, rpg2)
            rpg1.default_attack(rpg2)
            print(rpg2)
            # player2()
            rpg2.default_attack(rpg1)
            print(rpg1)
        if not rpg1.is_alive:
            rpg2.score += 1
            print(f"{rpg2.name} wins round {battle + 1}")
        elif not rpg2.is_alive:
            rpg1.score += 1
            print(f"{rpg1.name} wins round {battle + 1}")
        print(f"{rpg1.name} Won {rpg1.score} rounds")
        print(f"{rpg2.name} Won {rpg2.score} rounds")
    if rpg1.score == rpg2.score:
        print(f"Competition is a tie")
    elif rpg1.score > rpg2.score:
        print(f"{rpg1.name} Wins the competition")
    else:
        print(f"{rpg2.name} Wins the competition")

def main():
    rpg1 = Hunter("Elowen", 12, 120, 6)
    rpg2 = Magician("Malric", 8, 90, 12)

    battle_simulator(rpg1, rpg2)

main()