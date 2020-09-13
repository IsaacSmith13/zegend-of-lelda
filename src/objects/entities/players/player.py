from src.models.entities import DEFAULT_MOVESPEED
from src.configuration.configuration import GLOBAL_OBJECT_SIZE, STARTING_X, STARTING_Y
from src.objects.entities.entity import Entity

FRAMES_PER_ANIMATION = 8


class Player(Entity):
    def __init__(self, height=GLOBAL_OBJECT_SIZE, width=GLOBAL_OBJECT_SIZE, x=STARTING_X, y=STARTING_Y):
        super().__init__(
            frames_per_animation=FRAMES_PER_ANIMATION,
            height=height,
            name=type(self).__name__.lower(),
            movespeed=DEFAULT_MOVESPEED,
            width=width,
            x=x,
            y=y
        )
