from src.models.entities import DEFAULT_MOVESPEED
from src.models.objects import GLOBAL_OBJECT_SIZE
from src.objects.entities.entity import Entity

FRAMES_PER_ANIMATION = 8


class Player(Entity):
    def __init__(self, height=GLOBAL_OBJECT_SIZE, width=GLOBAL_OBJECT_SIZE, x=0, y=0):
        super().__init__(
            frames_per_animation=FRAMES_PER_ANIMATION,
            height=height,
            name=type(self).__name__.lower(),
            movespeed=DEFAULT_MOVESPEED,
            width=width,
            x=x,
            y=y
        )
