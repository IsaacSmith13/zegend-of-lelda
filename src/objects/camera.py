import math
from dotmap import DotMap
from src.configuration.configuration import DISPLAY_HEIGHT, DISPLAY_WIDTH, GLOBAL_OBJECT_SIZE, TILE_BUFFER

SAFE_SPACE_IN_TILES = 2
SAFE_SPACE_IN_PIXELS = SAFE_SPACE_IN_TILES * GLOBAL_OBJECT_SIZE
BUFFERED_SAFE_SPACE_IN_PIXELS = (SAFE_SPACE_IN_TILES + TILE_BUFFER) * GLOBAL_OBJECT_SIZE


class Camera():
    def __init__(self, level_height, level_width, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH):
        self.boundaries = DotMap(
            right=DotMap(
                current=width - BUFFERED_SAFE_SPACE_IN_PIXELS,
                initial=width - BUFFERED_SAFE_SPACE_IN_PIXELS,
                final=level_width - BUFFERED_SAFE_SPACE_IN_PIXELS,
            ),
            bottom=DotMap(
                current=height - BUFFERED_SAFE_SPACE_IN_PIXELS,
                initial=height - BUFFERED_SAFE_SPACE_IN_PIXELS,
                final=level_height - BUFFERED_SAFE_SPACE_IN_PIXELS,
            ),
            left=DotMap(
                current=SAFE_SPACE_IN_PIXELS,
                initial=SAFE_SPACE_IN_PIXELS,
                final=level_width - width + SAFE_SPACE_IN_PIXELS
            ),
            top=DotMap(
                current=SAFE_SPACE_IN_PIXELS,
                initial=SAFE_SPACE_IN_PIXELS,
                final=level_height - height + SAFE_SPACE_IN_PIXELS
            )
        )

        self.height = height
        self.width = width

        self.last_x = 0
        self.last_y = 0
        self.x = 0
        self.y = 0

    def get_x(self):
        return self.x

    def get_x_in_tiles(self):
        return math.floor(self.x / GLOBAL_OBJECT_SIZE)

    def get_x_offset(self):
        return 0 - self.x % GLOBAL_OBJECT_SIZE

    def get_y(self):
        return self.y

    def get_y_in_tiles(self):
        return math.floor(self.y / GLOBAL_OBJECT_SIZE)

    def get_y_offset(self):
        return 0 - self.y % GLOBAL_OBJECT_SIZE

    def set_x(self, x):
        moving_right = x > self.last_x
        moving_left = x < self.last_x

        can_push_right_boundary = x > self.boundaries.right.current and x < self.boundaries.right.final
        can_push_left_boundary = x < self.boundaries.left.current and x < self.boundaries.left.final

        if (moving_right and can_push_right_boundary) or (moving_left and can_push_left_boundary):
            x_diff = x - self.last_x

            self.boundaries.right.current = min(max(self.boundaries.right.current + x_diff, self.boundaries.right.initial), self.boundaries.right.final)
            self.boundaries.left.current = min(max(self.boundaries.left.current + x_diff, self.boundaries.left.initial), self.boundaries.left.final)

            self.x = max(self.x + x_diff, 0)

        self.last_x = x

    def set_y(self, y):
        moving_down = y > self.last_y
        moving_up = y < self.last_y

        can_push_bottom_boundary = y > self.boundaries.bottom.current and y < self.boundaries.bottom.final
        can_push_top_boundary = y < self.boundaries.top.current and y < self.boundaries.top.final

        if (moving_down and can_push_bottom_boundary) or (moving_up and can_push_top_boundary):
            y_diff = y - self.last_y

            self.boundaries.bottom.current = min(max(self.boundaries.bottom.current + y_diff, self.boundaries.bottom.initial), self.boundaries.bottom.final)
            self.boundaries.top.current = min(max(self.boundaries.top.current + y_diff, self.boundaries.top.initial), self.boundaries.top.final)

            self.y = max(self.y + y_diff, 0)

        self.last_y = y
