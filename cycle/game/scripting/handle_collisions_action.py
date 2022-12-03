import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

import random

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the other cycle, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self, first_cycle, second_cycle):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._first_cycle = first_cycle
        self._second_cycle = second_cycle
        self._winner = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_time_passes(cast)
            self._handle_other_segment_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    def _handle_time_passes(self, cast):
        """Cycle's track randomly grows...1% of the time.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_specific_actor("cycles", 1)
        cycle2 = cast.get_specific_actor("cycles", 2)
        to_increase_or_not_to_increase1 = random.choice([
            True, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False
        ])
        to_increase_or_not_to_increase2 = random.choice([
            True, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False, 
            False, False, False, False, False, False, False, False, False, False,
            False, False, False, False, False, False, False, False, False, False
        ])
        if to_increase_or_not_to_increase1:
            cycle1.grow_tail(1)
        if to_increase_or_not_to_increase2:
            cycle2.grow_tail(1)
    
    def _handle_other_segment_collision(self, cast):
        """Sets the game over flag and adds the winning score to the player who got hit if the cycle collides with the other cycle.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_specific_actor("cycles", 1)
        score1 = cast.get_specific_actor("scores", 1)
        cycle2 = cast.get_specific_actor("cycles", 2)
        score2 = cast.get_specific_actor("scores", 2)

        for segment in cycle1.get_segments()[1:]:
            if cycle2.get_segments()[0].get_position().equals(segment.get_position()):
                score1.add_points(1)
                self._winner = " Player 1 wins!"
                self._is_game_over = True
                break
        
        for segment in cycle2.get_segments()[1:]:
            if cycle1.get_segments()[0].get_position().equals(segment.get_position()):
                score2.add_points(1)
                self._winner = " Player 2 wins!"
                self._is_game_over = True
                break
        
        if cycle1.get_segments()[0].get_position().equals(cycle2.get_segments()[0].get_position()):
            self._winner = " Head-on collision! Both players lose!"
            self._is_game_over = True

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_specific_actor("cycles", 1)
        cycle2 = cast.get_specific_actor("cycles", 2)
        
        for cycle in [cycle1, cycle2]:
            for segment in cycle.get_segments()[1:]:
                if cycle.get_segments()[0].get_position().equals(segment.get_position()):
                    self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle1 = cast.get_specific_actor("cycles", 1)
            segments1 = cycle1.get_segments()
            cycle2 = cast.get_specific_actor("cycles", 2)
            segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"Game Over!{self._winner}")
            message.set_position(position)
            cast.add_actor("messages", message)

            for cycle in [segments1, segments2]:
                for segment in cycle:
                    segment.set_color(constants.WHITE)
