""" Opgave "Number guessing"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

--------

Opret et program, der spiller et gættespil med brugeren. Programmet fungerer på følgende måde:
    Forklar reglerne for brugeren.
    Generer tilfældigt et 4-cifret heltal.
    Bed brugeren om at gætte et 4-cifret tal.
    Hvert ciffer, som brugeren gætter korrekt i den rigtige position, tæller som en sort mønt.
    Hvert ciffer, som brugeren gætter korrekt, men i den forkerte position, tæller som en hvid mønt.
    Når brugeren har gættet, udskrives det, hvor mange sorte og hvide mønter gættet er værd.
    Lad brugeren gætte, indtil gættet er korrekt.
    Hold styr på antallet af gæt, som brugeren gætter i løbet af spillet, og print det ud til sidst.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import random

def main():
    random_number = (generate_number())
    guess = "0"
    black_coins = 0
    white_coins = 0
    guess_counter = 0
    print("This is a number guessing game. Whenever you guess a correct number in the right position you receive a black coin. If you guess the correct number in the wrong position you get a white coin.")
    print("Please guess the 4 digit number:")
    while guess != random_number:
        guess_counter += 1
        guess = guessing_promt()
        if guess == "0":
            continue
        else:
            for i in range(4):
                if guess[i] == random_number[i]:
                    black_coins = earn_black_coin(black_coins)
                elif guess[i] in random_number:
                    white_coins = earn_white_coin(white_coins)
    print("You guessed the correct number!")
    print(f"You spent {guess_counter} guesses and got {black_coins} black coins and {white_coins} white coins")


def earn_white_coin(coin_amount):
    coin_amount += 1
    print("+ 1 white coin")
    return coin_amount


def earn_black_coin(coin_amount):
    coin_amount += 1
    print("+ 1 black coin")
    return coin_amount


def generate_number():
    random_number = f"{random.randint(0, 9999):04}"
    print(random_number)
    return random_number


def guessing_promt():
    guess = input()
    if len(guess) == 4 and guess.isdigit():
        return guess
    else:
        print("Please enter a valid 4 digit number")
        return "0"


main()
