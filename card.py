class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        self.orientation = None
        self.position = (-1, -1)
        self.end_position = (-1, -1)
        self.in_position = False
        self.slope = None

    # Calculate the end position of where the card should be drawn
    def calculate_end_position(self, id, number):
        if id == 0:
            if number == 1:
                self.end_position = (755, 550)
            else:
                self.end_position = (805, 550)

        elif id == 1:
            self.end_position = (400, 450)

        elif id == 2:
            self.end_position = (800, 300)

        else:
            self.end_position = (1200, 450)
        self.calculate_slope()

    # Calculate the slope between the start and end
    def calculate_slope(self):
        self.slope = (self.position[1] - self.end_position[1]) / (
            self.position[0] - self.end_position[0]
        )

    # Update the card position by the slope
    def update_position_by_slope(self, displacement):
        new_x = self.position[0] - displacement
        new_y = self.position[1] - (displacement * self.slope)
        self.position = (new_x, new_y)

        if abs(self.position[0] - self.end_position[0]) < 2 and abs(
            self.position[1] - self.end_position[1] < 2
        ):
            self.in_position = True
