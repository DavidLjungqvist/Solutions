"""Opgave "Turtle Hunt": Klasse definition og konstanter

Læs øvelsesbeskrivelsen i th1_exercise.py.
"""

import turtle  # this imports a library called "turtle". A library is (someone else's) python code, that you can use in your own program.
import random
from math import degrees

from th3_service import distance, direction


class PlayerName1(turtle.Turtle):

    def __init__(self):
        super().__init__()  # Here, this is equivalent to turtle.Turtle.__init__(self)
        self.orientation = 0  # used to keep track of the turtle's current orientation (the direction it is heading)

    def rotate_prey(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # self: the turtle that shall be rotated
        # positions: a list of tuples. Each tuple is a pair of coordinates (x,y).
        # positions[0] is the coordinate tuple of the prey. positions[0][0] is the x-coordinate of the prey.
        # positions[1], positions[2], positions[3] refer to the hunters.
        # for example is positions[3][1] the y-coordinate of the third hunter.

        # Example for use of the service functions distance() and direction
        # print(f'{distance(positions[0], positions[1])=}   {direction(positions[0], positions[1])=}')  # print distance and direction from prey to hunter1
        distance_list = []
        for i in range(1, 4):
            distance_list.append(int(distance(positions[0], positions[i])))
        min_distance = min(distance_list)
        closest_turtle_index = distance_list.index(min_distance)
        closest_turtle_direction = direction(positions[0], positions[closest_turtle_index + 1])

        turtle_backward = (self.orientation + 180) % 360
        degree = closest_turtle_direction - turtle_backward # When the turtle rotates the same amount each turn,  it will just run in a circle. Make this function smarter!
        x, y = positions[0]
        if abs(x) > 270:
            move_vertically = True
        else:
            move_vertically = False
        if abs(y) > 270:
            move_horizontally = True
        else:
            move_horizontally = False

        if move_vertically and closest_turtle_direction > 180:
            degree = 90 - self.orientation
        elif move_vertically and closest_turtle_direction < 180:
            degree = 270 - self.orientation
        elif move_horizontally and (closest_turtle_direction + 90) % 360 < 180:
            degree = 180 - self.orientation
        elif move_horizontally and (closest_turtle_direction + 90) % 360 > 180:
            degree = 360 - self.orientation
        # elif move_horizontally and move_vertically:
        self.orientation += degree
        self.orientation %= 360
        # print(self.orientation)
        return degree

    def rotate_hunter(self, positions):  # turtle will be turned right <degree> degrees. Use negative values for left turns.
        # Example for use of the service functions distance() and direction
        # print(f'{distance(self.position(), positions[0])=}   {direction(self.position(), positions[0])=}')  # print distance and direction from the current hunter to the prey
        degree = 1.5 # When the turtle rotates the same amount each turn,  it will just run in a circle. Make this function smarter!
        # distance(self.position, positions[0])
        direction_to_target = direction(self.position(), positions[0])
        degree = direction_to_target - self.orientation
        self.orientation += degree
        self.orientation %= 360
        # print(self.orientation)
        return degree


#  Insert the code of your sparring partner's turtle class here:
#
#
#
#


# change these global constants only for debugging purposes:
MAX_TURNS = 100       # Maximum number of turns in a hunt.                           In competition: probably 200.
ROUNDS = 1            # Each player plays the prey this often.                       In competition: probably 10.
STEP_SIZE = 3         # Distance each turtle moves in one turn.                      In competition: probably 3.
SPEED = 0             # Fastest: 10, slowest: 1, max speed: 0.                       In competition: probably 0.
CAUGHT_DISTANCE = 10  # Hunt is over, when a hunter is nearer to the prey than that. In competition: probably 10.


random.seed(2)  # use seed() if you want reproducible random numbers for debugging purposes. You may change the argument of seed().


class1 = PlayerName1  # (red prey) Replace PlayerName1 by your own class name here.
class2 = PlayerName1  # (green prey) For testing your code, replace PlayerName1 by your own class name here. Later replace this by your sparring partner's class name.
