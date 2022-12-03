import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A 2-wheeled cycle that leaves a track.
    
    The responsibility of Cycle is to move itself.
    """
    def __init__(self, first_cycle, second_cycle):
        super().__init__()
        self._first_cycle = first_cycle
        self._second_cycle = second_cycle
        self._segments = []
        if self._first_cycle:
            self.set_velocity(Point(0, constants.CELL_SIZE))
            self._prepare_body()
        elif self._second_cycle:
            self.set_velocity(Point(0, -constants.CELL_SIZE))
            self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            if self._first_cycle:
                segment.set_color(constants.GREEN)
            elif self._second_cycle:
                segment.set_color(constants.ORANGE)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        if self._first_cycle:
            x = int(constants.MAX_X / 4)
        elif self._second_cycle:
            x = int(constants.MAX_X / 4 * 3)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.CYCLE_LENGTH):
            if self._first_cycle:
                position = Point(x, y - i * constants.CELL_SIZE)
                velocity = Point(0, constants.CELL_SIZE)
                color = constants.YELLOW if i == 0 else constants.GREEN
            elif self._second_cycle:
                position = Point(x, y - i * constants.CELL_SIZE)
                velocity = Point(0, constants.CELL_SIZE)
                color = constants.PURPLE if i == 0 else constants.ORANGE
            text = "8" if i in [0, 2] else "#"
            #color = constants.YELLOW if i == 0 else constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)