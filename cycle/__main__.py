import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("cycles", Cycle(first_cycle=True, second_cycle=False))
    cast.add_actor("cycles", Cycle(first_cycle=False, second_cycle=True))
    cast.add_actor("scores", Score(first_cycle=True, second_cycle=False))
    cast.add_actor("scores", Score(first_cycle=False, second_cycle=True))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service, first_cycle=True, second_cycle=False))
    script.add_action("input", ControlActorsAction(keyboard_service, first_cycle=False, second_cycle=True))
    script.add_action("update", MoveActorsAction(first_cycle=True, second_cycle=False))
    script.add_action("update", MoveActorsAction(first_cycle=False, second_cycle=True))
    script.add_action("update", HandleCollisionsAction(first_cycle=True, second_cycle=False))
    script.add_action("update", HandleCollisionsAction(first_cycle=False, second_cycle=True))
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()