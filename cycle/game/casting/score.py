import constants

from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, first_cycle, second_cycle):
        super().__init__()
        self._points = 0
        self._first_cycle = first_cycle
        self._second_cycle = second_cycle
        if self._first_cycle:
            self._player_num = 1
        elif self._second_cycle:
            self._player_num = 2
            self.set_position(Point(int(constants.MAX_X / 2), 0))
        self.set_text(f"Player {self._player_num}: {self._points}")
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Player {self._player_num}: {self._points}")

    def get_score(self):
        return self._points