class Action:
    """A thing that is done.
    
    The responsibility of action is to do somthing that is integral or important in the game. Thus,
    it has one method, execute(), which should be overridden by derived classes.
    """

    def __init__(self):
        pass
    
    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        raise NotImplementedError("You failed polymorphism class")
        
        
        
        
        #for member in cast:
        #    for action in script.get_actions.keys():
        #        member.action()