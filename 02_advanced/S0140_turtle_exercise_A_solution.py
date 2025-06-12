"""
Opgave "Tom the Turtle":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

-------

Denne opgave findes i varianterne A og B. Spørg din lærer, hvilken variant du skal arbejde med.

Del 0:
    Funktionen demo introducerer dig til alle de kommandoer, du skal bruge
    for at interagere med Tom the Turtle i de følgende øvelser.
    Find ud af hvad funktionen gør ved at lege med funktionskoden.
    Hvad gør fx funktionerne forward(), left(), right(), done()?

Del 1:
    Skriv en funktion "square", som accepterer en parameter "length".
    Hvis denne funktion kaldes, får skildpadden til at tegne en firkant med en sidelængde på "længde" pixels.

Del 2:
    Skriv en funktion "many_squares" med en for-loop, som kalder square gentagne gange.
    Brug denne funktion til at tegne flere firkanter af forskellig størrelse i forskellige positioner.
    Funktionen skal have nogle parametre. F.eks:
        antal: hvor mange firkanter skal der tegnes?
        størrelse: hvor store er firkanterne?
        afstand: hvor langt væk fra den sidste firkant er den næste firkant placeret?

Del 3:
    Skriv en funktion, der producerer mønstre, der ligner dette:
    https://pixabay.com/vectors/spiral-square-pattern-black-white-154465/

Del 4:
    Skriv en funktion, der producerer mønstre svarende til dette:
    https://www.101computing.net/2d-shapes-using-python-turtle/star-polygons/
    Funktionen skal have en parameter, som påvirker mønsterets form.

Del 5:
    Opret din egen funktion, der producerer et sejt mønster.

Kun hvis du er nysgerrig og elsker detaljer:
    Her er den fulde dokumentation for turtle graphics:
    https://docs.python.org/3.3/library/turtle.html

-------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Fortsæt derefter med den næste fil.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
from math import gcd

def demo():  # demonstration of basic turtle commands
    tom.speed(8)  # fastest: 10, slowest: 1
    for x in range(8):  # do the following for x = 0, 1, 2, 3, 4, 5, 6, 7
        tom.forward(50)  # move 50 pixels
        tom.left(45)  # turn 45 degrees left
        print(f'Tom is now at {tom.position()}, x-value: {tom.position()[0]=:.2f}, y-value: {tom.position()[1]=:.2f}')
    tom.penup()  # do not draw while moving from now on
    tom.forward(100)
    tom.pendown()  # draw while moving from now on
    tom.circle(50)  # draw a circle with radius 50
    tom.pencolor("red")  # draw in red
    tom.right(90)  # turn 90 degrees right
    tom.forward(120)
    tom.right(-90)  # turning -90 degrees right is the same as turning +90 degrees left
    tom.forward(120)
    tom.goto(-100, -200)  # move to coordinates -100, -200  (0, 0 is the middle of the screen)
    tom.home()  # return to the original position in the middle of the window

def square(lenght):
    tom.speed(8)
    for x in range(4):
        tom.forward(lenght)  # move 50 pixels
        tom.left(90)  # turn 45 degrees left



def many_squares(quantity, size, distance):
    tom.speed(8)
    for y in range(quantity):
        for x in range(4):
            tom.forward(size)
            tom.left(90)
        tom.penup()
        tom.forward(distance)
        tom.pendown()


def spiral(size):
    tom.speed(8)
    while size > 0:
        tom.forward(size)
        tom.right(90)
        size = size - 4

def highest_valid_k(angles):
    for k in range(angles//2, 1, -1):  # Starter fra det største spring under angles/2 og går ned til 2
        if gcd(angles, k) == 1:
            return k
    return None


# def lowest_valid_k(angles):
#     for k in range(2, angles // 2 + 1):  # k > 1 og k < angles/2
#         if gcd(angles, k) == 1:
#             return k
#     return None  # Ingen gyldig stjerne


def star(angles, size, speed=8):
    k = highest_valid_k(angles)
    tom.speed(speed)
    if k is not None:
        for x in range(angles):
            tom.forward(size)
            tom.right(round((360 * k / angles), 2))
    else:
        print("invalid amount of angles")


def cube(size):
    tom.speed(5)
    tom.left(35)
    tom.forward(size)
    tom.left(55)
    tom.forward(size)
    tom.left(125)
    tom.forward(size)
    tom.left(55)
    tom.forward(size)
    tom.right(125)
    tom.forward(size)
    tom.right(55)
    tom.forward(size)
    tom.right(125)
    tom.forward(size)
    tom.left(70)
    tom.forward(size)
    tom.left(110)
    tom.forward(size)
    tom.left(70)
    tom.forward(size)


tom = turtle.Turtle()  # create an object named tom of type Turtle

# demo()

# square(50)

# many_squares(3, 50, 100)

# spiral(80)

star(9, 200)

# cube(100)

turtle.done()  # keep the turtle window open after the program is done
