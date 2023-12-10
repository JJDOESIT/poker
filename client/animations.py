from server.vector import Vector


class Animations:
    def __init__(self):
        pass

    # Linear interpolation with vector
    def lerp_position(self, position: Vector, end_position: Vector, tick: float):
        position = position * (1 - tick) + end_position * tick
        return position

    # Linear interpolation with number
    def lerp_number(self, number: float, end_number: float, tick: float):
        n = number * (1 - tick) + end_number * tick
        return n
