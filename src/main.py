"""
    Main class for application.
"""
# helper
import sys
# graphic
from ursina import Ursina, held_keys, Text, color
from ursina.prefabs.first_person_controller import FirstPersonController
# app moduls
from location.location import Location
from astar.astar import AStar
from utils.settings import BASE


class App:
    """
    Main class for application.

    Attributes:
        app - Ursina - create window and init application.
        astar - AStar - generate location and find path from start to end.
        player - Player - object for user. Using this class, user can move inside the location.
        path_found - bool - True if path was found, False otherwise.
        Uses to optimyze path searching.

        b_count - Text - object, that print count of barriers.
        path_size - Text - object, that print count of blocks in path from start to end.
        Off until user presses enter.
        warn_mess - Text - object, that print warning message if path from start to end not found.
    """

    def __init__(self):
        """Initialize whole application."""
        self.app = Ursina(size=(BASE['WIDTH'], BASE['HEIGHT']))
        self.astar = AStar(Location())
        self.player = FirstPersonController(position=(10, 10, 10))
        self.path_found = False
        self.b_count = Text(text=f'Count of barriers: {len(self.astar.graph.entities) - 2}',
                            origin=(0, -8), color=color.yellow, scale=2)
        self.path_size = Text(text=f'Path size: {len(self.astar.graph.path_entities)}',
                              origin=(0, -6), color=color.yellow, scale=2)
        self.warn_mess = Text(text='Path not found!', origin=(0, 0), color=color.yellow, scale=2)
        self.path_size.disable()
        self.warn_mess.disable()

    def run(self) -> None:
        """Main loop of application. Runs until user presses escape.
        How work:
            escape - close application.
            1 - regenerate location including start and end position.
            2 - generate new barriers to exists barriers.
            enter - find path using AStar algorithm.
        """
        while True:
            if held_keys['escape']:
                sys.exit()
            elif held_keys['1']:
                self.astar.graph.set_location()
                self.path_found = False
                self.path_size.disable()
                self.warn_mess.disable()
            elif held_keys['2']:
                self.astar.graph.generate_barriers(BASE['INCREASE_BARRIER_COUNT'])
            elif held_keys['enter']:
                self.run_astar()
            self.b_count.text = f'Count of barriers: {len(self.astar.graph.entities) - 2}'
            self.app.step()

    def run_astar(self) -> None:
        """Run AStar algorithm and if path not found, print warning message."""
        if self.astar.find_path() is False and self.path_found is False:
            self.warn_mess.enable()
        else:
            self.path_found = True
            self.astar.draw_path()
            self.path_size.text = f'Path size: {len(self.astar.graph.path_entities)}'
            self.path_size.enable()


if __name__ == '__main__':
    App().run()
