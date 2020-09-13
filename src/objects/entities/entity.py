from src.configuration.configuration import GLOBAL_OBJECT_SIZE
from src.models.entities import DIRECTIONS
from src.objects.entities.sprite_sheet import SpriteSheet, ENTITIES
from src.objects.object import Object


class Entity(Object):
    def __init__(
            self,
            frames_per_animation,
            name,
            movespeed,
            x,
            y,
            height=GLOBAL_OBJECT_SIZE,
            width=GLOBAL_OBJECT_SIZE
    ):
        self.current_directions = []
        self.movespeed = movespeed

        self.sprite_sheet = SpriteSheet(
            ENTITIES[name],
            frames_per_animation=frames_per_animation,
            height=height,
            width=width
        )

        super().__init__(
            collidable=True,
            image=self.sprite_sheet.get_frame(),
            height=height,
            width=width,
            x=x,
            y=y
        )

    def get_movespeed(self):
        return self.movespeed

    def set_movespeed(self, movespeed):
        self.movespeed = movespeed

    def add_direction(self, direction):
        if direction not in self.current_directions:
            self.current_directions.append(direction)

    def remove_direction(self, direction):
        if direction in self.current_directions:
            self.current_directions.remove(direction)

    def tick(self, delta):
        if len(self.current_directions) == 0:
            self.sprite_sheet.reset_frame()
        else:
            right = down = left = up = False

            for direction in self.current_directions:
                if direction == DIRECTIONS.right and not left:
                    right = True
                    self.set_x(self.x + self.movespeed * delta)
                elif direction == DIRECTIONS.down and not up:
                    down = True
                    self.set_y(self.y + self.movespeed * delta)
                elif direction == DIRECTIONS.left and not right:
                    left = True
                    self.set_x(self.x - self.movespeed * delta)
                elif direction == DIRECTIONS.up and not down:
                    up = True
                    self.set_y(self.y - self.movespeed * delta)

            self.sprite_sheet.update_frame(delta=delta, direction=self.current_directions[0])

        self.image = self.sprite_sheet.get_frame()
