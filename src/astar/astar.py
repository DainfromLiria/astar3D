"""
    Implementation of AStar algorithm for 3D location.
"""
# helper
from queue import PriorityQueue
# graphic
from ursina import color
# app moduls
from utils.support import manh_dist, is_in_range, draw_cube
from utils.settings import STATES
from location.location import Location


class AStar:
    """Implementation of AStar algorithm for 3D location.

    Attributes:
        graph - Location - current location with barriers, start and end positions.
        offset - List[Tuple[int, int, int]] - List with offsets,
        that is used to calculate neighbours of the position."""

    def __init__(self, graph: Location):
        """Initializes AStar algorithm."""
        self.graph = graph
        self.offset = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    def find_path(self) -> bool:
        """Using AStar algorithm find path from position start to position end.

        Return:
            bool - True if path is found, False otherwise.
        """
        to_visit = PriorityQueue()
        to_visit.put((0, self.graph.start))

        self.graph.set_state(self.graph.start, STATES['FOUND'])
        self.graph.set_dist(self.graph.start, 0)

        while not to_visit.empty():
            curr = to_visit.get()[1]

            # end point was found
            if curr == self.graph.end:
                return True

            for x, y, z in self.offset:
                nb = (curr[0] - x, curr[1] - y, curr[2] - z)  # get neighbour
                # distance(Dijkstra) + heuristic
                new_dist = 1 + self.graph.get_dist(curr) + manh_dist(nb, self.graph.end)

                # add to queue if we do not visit this position
                # OR if value of heuristic function is less than current value for his position
                if (is_in_range(nb) and
                        (self.graph.check_state(nb, STATES['FREE']) or
                         new_dist < self.graph.get_dist(nb))):
                    to_visit.put((new_dist, nb))
                    self.graph.set_prev(nb, curr)
                    self.graph.set_state(nb, STATES['FOUND'])
                    self.graph.set_dist(nb, self.graph.get_dist(curr) + 1)
        return False

    def draw_path(self) -> None:
        """Backtrack the path and draw it."""
        tmp = self.graph.end
        while tmp != self.graph.start:
            draw_cube(self.graph.get_prev(tmp), color.green)
            tmp = self.graph.get_prev(tmp)
