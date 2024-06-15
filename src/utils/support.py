"""
    Support functions for A* algorithm
"""
# helper
from math import sqrt
from typing import Tuple
from random import randint
# graphic
from ursina import Entity, scene
# app moduls
from utils.settings import LIMITS


def manh_dist(p_start: Tuple[int, int, int], p_end: Tuple[int, int, int]) -> int:
    """Calculate Manhattan distance in 3D.

    Attributes:
        p_start - Tuple[int, int, int] - begin point.
        p_end - Tuple[int, int, int] - end point.

    Return:
        int - Manhattan distance from point p_start to point p_end.
    """
    return sum(abs(e - s) for s, e in zip(p_start, p_end))


def euklid_dist(p_start: Tuple[int, int, int], p_end: Tuple[int, int, int]) -> float:
    """Calculate Euclidean distance in 3D.

    Attributes:
        p_start - Tuple[int, int, int] - begin point.
        p_end - Tuple[int, int, int] - end point.

    Return:
        int - Euclidean distance from point p_start to point p_end.
    """
    return sqrt(sum((e - s) ** 2 for s, e in zip(p_start, p_end)))


def is_wall(x: int, y: int, z: int) -> bool:
    """Check if input position is position in wall, floor or roof.

    Attributes:
        x - int - x coordinate.
        y - int - y coordinate.
        z - int - z coordinate.

    Return:
        bool - True if position is inside wall, floor or roof, False otherwise.
    """
    return (x == LIMITS['x_max'] - 1 or x == 0
            or y == LIMITS['y_max'] - 1 or y == 0
            or z == LIMITS['z_max'] - 1 or z == 0)


def get_random_pos() -> Tuple[int, int, int]:
    """Generate random position inside location.

    Return:
        Tuple[int, int, int] - random position inside location, in format (x, y, z).
    """
    x = randint(1, (LIMITS['x_max'] - 2))
    y = randint(1, (LIMITS['y_max'] - 2))
    z = randint(1, (LIMITS['z_max'] - 2))
    return x, y, z


def draw_cube(pos: Tuple[int, int, int], color) -> Entity:
    """Draw a cube on position pos using input color.

    Attributes:
        pos - Tuple[int, int, int] - input position, where we want to draw a cube.
        color - ursina.color - cube color.
    Return:
        Entity - cube object
    """
    e = Entity(model="cube", color=color, position=pos,
               parent=scene,
               collider="box",
               texture="white_cube",
               origin_y=0.5,
               ignore=True
               )
    return e


def is_in_range(pos: Tuple[int, int, int]) -> bool:
    """Check if input position is inside location.

    Attributes:
        pos - Tuple[int, int, int] - input position.

    Return:
        bool - True if position is inside location, False otherwise.
    """
    for p, h in zip(pos, (LIMITS['x_max'] - 1, LIMITS['y_max'] - 1, LIMITS['z_max'] - 1)):
        if p >= h or p <= 0:
            return False
    return True
