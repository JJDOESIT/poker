import math
from vector import Vector


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.position = Vector(-1, -1)
        self.end_position = Vector(-1, -1)
        self.angle = 0
        self.end_angle = None
        self.distance = None
        self.tick = 0.01
        self.in_position = False
        self.slope = None

    # Calculate the end position of where the card should be drawn
    def calculate_end_position(self, id, number):
        if id == 0:
            if number == 1:
                self.end_position.x = 755
                self.end_position.y = 550
            else:
                self.end_position.x = 805
                self.end_position.y = 550
        elif id == 1:
            if number == 1:
                self.end_position.x = 425
                self.end_position.y = 450
            else:
                self.end_position.x = 425
                self.end_position.y = 400
        elif id == 2:
            if number == 1:
                self.end_position.x = 755
                self.end_position.y = 290
            else:
                self.end_position.x = 805
                self.end_position.y = 290
        else:
            if number == 1:
                self.end_position.x = 1100
                self.end_position.y = 450
            else:
                self.end_position.x = 1100
                self.end_position.y = 400

        self.calculate_slope()
        self.distance = self.calculate_distance()

    # Calculate the diagonal distance between the current position and the end position
    def calculate_distance(self):
        return math.sqrt(
            math.pow(self.position.x - self.end_position.x, 2)
            + math.pow(self.position.y - self.end_position.y, 2)
        )

    # Calculate the slope between the start and end
    def calculate_slope(self):
        self.slope = (self.position.y - self.end_position.y) / (
            self.position.x - self.end_position.x
        )

    # Spherical linear interpolation
    def slerp(self):
        self.angle = self.angle * (1 - self.tick) + self.end_angle * self.tick

    # Linear interpolation
    def lerp(self):
        self.position = self.position * (1 - self.tick) + self.end_position * self.tick
        self.tick += 0.01
        self.check_if_in_position()

    # Check if the card is in its final position
    def check_if_in_position(self):
        difference = self.position - self.end_position
        if abs(difference.x) <= 0.05 and abs(difference.y) <= 0.05:
            self.in_position = True
            self.position = self.end_position
            self.angle = self.end_angle
            return True
        return False

    # Set the orientation of the card
    def set_orientation(self, id, rotations):
        if id % 2 == 0:
            self.end_angle = rotations * 360
        else:
            self.end_angle = (rotations * 360) + 90
