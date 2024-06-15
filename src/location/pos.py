"""
    Class represented one cube (position) in 3D location
"""
# helper
from math import inf
from typing import Tuple
# app moduls
from utils.settings import STATES


class Pos:
    """
        Class represented one cube (position) in 3D location.

        Attributes:
            prev - Tuple[int, int, int] - previous position.
            We were in this position in previous step of the AStar algorithm.

            state - int - state of this position. By default, FREE. Can be:
                1 - BARRIER - wall, floor or roof
                2 - FREE - empty space
                3 - FOUND - visited position

            dist - int - distance from start.
            On the beginning of the AStar algorithm, all positions is
            on the max distance from start point, so we can use inf.
    """
    def __init__(self, state: int = STATES['FREE']):
        """Initialize one position."""
        self.prev = (-1, -1, -1)
        self.state = state
        self.dist = inf

    def check_state(self, state: int) -> bool:
        """Check if input state is same with state of current position.
        Attributes:
            state - int - state of this position. Valid values is documented in the class docstring.
        Return:
            bool - True if states are same, False otherwise.
        """
        return self.state == state

    def get_prev(self) -> Tuple[int, int, int]:
        """Return previous position set during AStar algorithm."""
        return self.prev

    def set_prev(self, prev: Tuple[int, int, int]) -> None:
        """Set new previous position.
        Attributes:
            prev - Tuple[int, int, int] - previous position in 3D location.
        """
        self.prev = prev

    def set_dist(self, dist: float) -> None:
        """Set new distance to start position.
        Attributes:
            dist - int - new distance to start.
        """
        self.dist = dist

    def get_dist(self) -> float:
        """Return distance to start position."""
        return self.dist

    def set_state(self, state: int) -> None:
        """Set new state of this position.
        Attributes:
            state - int - new state.
        """
        self.state = state
