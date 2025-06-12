"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""


morris = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}

def sleep():
    morris["sleepiness"] -= 10
    morris["thirst"] += 1
    morris["hunger"] += 1


def mine():
    morris["sleepiness"] += 5
    morris["thirst"] += 5
    morris["hunger"] += 5
    morris["gold"] += 5


def eat():
    morris["sleepiness"] += 5
    morris["thirst"] -= 5
    morris["hunger"] -= 20
    morris["gold"] -= 2


def buy_whisky():
    morris["sleepiness"] += 5
    morris["thirst"] += 1
    morris["hunger"] += 1
    morris["whisky"] += 1
    morris["gold"] -= 1


def drink():
    morris["sleepiness"] += 5
    morris["thirst"] -= 15
    morris["hunger"] -= 1
    morris["whisky"] -= 1


def dead():
    return morris["sleepiness"] > 100 or morris["thirst"] > 100 or morris["hunger"] > 100


while not dead() and morris["turn"] < 1000:
    morris["turn"] += 1
    if morris["sleepiness"] > 90:
        sleep()
    elif morris["thirst"] >= 95 and morris["whisky"] > 0:
        drink()
    elif morris["thirst"] >= 90 and morris["whisky"] == 0:
        buy_whisky()
    elif morris["hunger"] > 90:
        eat()
    else:
        mine()

    print(morris)
