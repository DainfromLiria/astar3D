"""
    Class represented 3D location.
"""
# helper
from math import inf
from itertools import product
from typing import Tuple
# graphic
from ursina import color
# app moduls
from utils.settings import BASE, LIMITS, STATES
from utils.support import is_wall, get_random_pos, draw_cube
from location.pos import Pos


class Location:
    """
        Class represented 3D location.
        location - Dict[Tuple[int, int, int], Pos] - dictionary that represented location.
        Key is position and value is Pos object.

        start - Tuple[int, int, int] - begin position.
        end - Tuple[int, int, int] - end position.
    """
    def __init__(self):
        """Create and set location."""
        self.location = {}
        self.start = None
        self.end = None
        self.create_location()
        self.set_location()

    def get_prev(self, pos: Tuple[int, int, int]) -> Tuple[int, int, int]:
        """Return the previous position of the input position.
        Return:
            Tuple[int, int, int] - previous position of position pos.
            (-1, -1, -1) - if position has not already found or if position is start position.
            """
        return (-1, -1, -1) if pos not in self.location else self.location[pos].get_prev()

    def set_prev(self, pos: Tuple[int, int, int], prev: Tuple[int, int, int]) -> None:
        """Set the previous position of the position pos.
        If position does not exist, then create position with default state (FREE).

        Attributes:
            pos - Tuple[int, int, int] - current position.
            prev - Tuple[int, int, int] - previous position.
        """
        if pos not in self.location:
            self.location[pos] = Pos()
        self.location[pos].set_prev(prev)

    def get_dist(self, pos: Tuple[int, int, int]) -> int:
        """Return the distance from pos to start.
        If pos does not exist, then return inf.

        Attributes:
            pos - Tuple[int, int, int] - current position.

        Return:
            int - distance from pos to start.
        """
        return inf if pos not in self.location else self.location[pos].get_dist()

    def set_dist(self, pos: Tuple[int, int, int], dist: int) -> None:
        """Set new distance for the position pos.
        If position does not exist, then create position with default state (FREE).

        Attributes:
            pos - Tuple[int, int, int] - current position.
            dist - int - new distance from pos to start.
        """
        if pos not in self.location:
            self.location[pos] = Pos()
        self.location[pos].set_dist(dist)

    def check_state(self, pos: Tuple[int, int, int], state: int) -> int:
        """Compare input state with current pos state.
        If pos does not exist, then compare with default position state => FREE.

        Attributes:
            pos - Tuple[int, int, int] - current position.
            state - int - input state.
        Return:
            bool - True if input state is same with current pos state, else False.
        """
        if pos in self.location:
            return self.location[pos].check_state(state)
        return STATES['FREE'] == state

    def set_state(self, pos: Tuple[int, int, int], state: int) -> None:
        """Set state for the position pos.
        If position does not exist, then create position with default state (FREE).

        Attributes:
            pos - Tuple[int, int, int] - current position.
            state - int - new state.
        """
        if pos not in self.location:
            self.location[pos] = Pos()
        self.location[pos].set_state(state)

    def create_location(self) -> None:
        """Create and draw location. Create walls, roof and floor."""
        for x, y, z in product(range(LIMITS['x_max']), range(LIMITS['y_max']),
                               range(LIMITS['z_max'])):
            if is_wall(x, y, z):
                self.location[(x, y, z)] = Pos(STATES['BARRIER'])
                draw_cube((x, y, z), color.dark_gray)

    def set_location(self) -> None:
        """Set location. Generate barriers, start and finish points."""
        # create barriers
        for _ in range(BASE['BARRIER_COUNT']):
            r_pos = get_random_pos()
            self.location[r_pos] = Pos(STATES['BARRIER'])
            draw_cube(r_pos, color.red)

        # generate start and finish.
        while self.start is None or self.end is None:
            # create start
            if self.start is None:
                s_pos = get_random_pos()
                if s_pos not in self.location:
                    self.start = s_pos
                    self.location[s_pos] = Pos(STATES['FREE'])
                    draw_cube(s_pos, color.blue)
            # create finish
            if self.end is None:
                e_pos = get_random_pos()
                if e_pos not in self.location:
                    self.end = e_pos
                    self.location[e_pos] = Pos(STATES['FREE'])
                    draw_cube(e_pos, color.pink)
