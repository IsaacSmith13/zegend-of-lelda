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
            if direction == DIRECTIONS.right and DIRECTIONS.left not in self.current_directions:
                self.current_directions.append(direction)
            elif direction == DIRECTIONS.left and DIRECTIONS.right not in self.current_directions:
                self.current_directions.append(direction)
            elif direction == DIRECTIONS.down and DIRECTIONS.up not in self.current_directions:
                self.current_directions.append(direction)
            elif direction == DIRECTIONS.up and DIRECTIONS.down not in self.current_directions:
                self.current_directions.append(direction)

    def remove_direction(self, direction):
        if direction in self.current_directions:
            self.current_directions.remove(direction)

    def tick(self, delta):
        if len(self.current_directions) == 0:
            self.sprite_sheet.reset_frame()
        else:
            for direction in self.current_directions:
                if direction == DIRECTIONS.right:
                    self.set_x(self.x + self.movespeed * delta)
                elif direction == DIRECTIONS.down:
                    self.set_y(self.y + self.movespeed * delta)
                elif direction == DIRECTIONS.left:
                    self.set_x(self.x - self.movespeed * delta)
                elif direction == DIRECTIONS.up:
                    self.set_y(self.y - self.movespeed * delta)

            self.sprite_sheet.update_frame(delta=delta, direction=self.current_directions[0])

        self.image = self.sprite_sheet.get_frame()
