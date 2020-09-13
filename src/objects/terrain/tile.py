from src.configuration.configuration import GLOBAL_OBJECT_SIZE
from src.objects.object import Object


class Tile(Object):
    def __init__(self, collidable, image, x, y, height=GLOBAL_OBJECT_SIZE, width=GLOBAL_OBJECT_SIZE):
        super().__init__(collidable=collidable, image=image, height=height, width=width, x=x, y=y)
