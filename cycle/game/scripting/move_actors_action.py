from game.scripting.action import Action


class MoveActorsAction(Action):
    
    def __init__(self, first_cycle, second_cycle):
        self._second_cycle = second_cycle
        self._first_cycle = first_cycle
        self._second_cycle = second_cycle
    
    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
