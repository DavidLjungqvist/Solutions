"""
Opgave "Cars":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Definer en funktion drive_car(), der udskriver en bils motorlyd (f.eks. "roooaar")

I hovedprogrammet:
    Definer variabler, som repræsenterer antallet af hjul og den maksimale hastighed for 2 forskellige biler
    Udskriv disse egenskaber for begge biler
    Kald derefter funktionen drive_car()

Hvis du ikke har nogen idé om, hvordan du skal begynde, kan du åbne S0420_cars_help.py og starte derfra.
Hvis du går i stå, kan du spørge google, de andre elever, en AI eller læreren.
Hvis du stadig er gået i stå, skal du åbne S0430_cars_solution.py og sammenligne den med din løsning.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Team-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""


def main():
    car_1_wheel_amount = 4
    car_1_top_speed = 180
    car_2_wheel_amount = 3
    car_2_top_speed = 135
    print(f"This car has {car_1_wheel_amount} wheels and a top speed of {car_1_top_speed}km/h")
    drive_car_1()
    print(f"This car has {car_2_wheel_amount} wheels and a top speed of {car_2_top_speed}km/h")
    drive_car_2()


def drive_car_1():
    print("Wroooooooom!!")


def drive_car_2():
    print("Wrooom!")


main()
