import pygame as pg
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

    # Rotate an image
    def rotate_image(self, image: pg.image, angle: float):
        rotated_image = pg.transform.rotate(
            image, angle
        )
        return rotated_image

    # Scale an image
    def scale_image(self, image: pg.image, width: float, height: float):
        scaled_image = pg.transform.scale(
            image, (width, height)
        )
        return scaled_image
