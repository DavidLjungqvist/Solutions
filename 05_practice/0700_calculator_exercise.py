""" Øvelse: "Calculator"

Som altid, læs hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning i kopien.

-------

Opret et program, der fungerer som en simpel lommeregner. Programmet skal fungere som følger:
    1. Forklar brugeren hvordan man betjener programmet.
    2. Præsenter en menu med følgende muligheder:
        - Addition
        - Subtraktion
        - Multiplikation
        - Division
        - Afslut
    3. Bed brugeren om at vælge en mulighed fra menuen.
    4. Hvis brugeren vælger en aritmetisk operation, bed om to tal.
    5. Udfør den valgte operation og vis resultatet.
    6. Gentag processen, indtil brugeren vælger at afslutte.

-------

Hvis du går i stå, spørg Google, andre elever, en AI eller læreren.

Når dit program er færdigt, skub det til dit GitHub-repository.
"""


def add(input1, input2):
    return input1 + input2


def subtract(input1, input2):
    return input1 - input2


def multiply(input1, input2):
    return input1 * input2


def divide(input1, input2):
    return input1 / input2


def main_program():
    command_number = 0
    command = str
    valid_commands = [1, 2, 3, 4]
    while command_number != 5:
        print(f"####################### CALCULATOR #######################\n   Please type in and enter a number for these commands:\n    1            2               3             4       5\n"
              "Addition / Substraction / Multiplication / Division / Exit")
        command_number = int(input())
        print(command_number)
        while command_number not in valid_commands:
            print(command_number)
            print("            You've entered an invalid command!")
            command_number = int(input())
        if command_number == 1:
            command = "addition"
        elif command_number == 2:
            command = "subtraction"
        elif command_number == 3:
            command = "multiplication"
        elif command_number == 4:
            command = "division"
        print(f"You've entered {command_number} for {command}\n What's the first number you would like to {command} with")
        first_number = float(input())

        print(f"What's the second number you would like to {command} with?")
        second_number = float(input())

        command_dic = {
            "addition": add,
            "subtraction": subtract,
            "multiplication": multiply,
            "division": divide
        }
        if command in command_dic:
            print(command_dic[command](first_number, second_number))

        if command == 5:
            print("            Thanks for using the calculator!")


main_program()
