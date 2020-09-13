from dotmap import DotMap

DIRECTIONS = DotMap(
    right=DotMap(name="right", value=0),
    down=DotMap(name="down", value=1),
    left=DotMap(name="left", value=2),
    up=DotMap(name="up", value=3)
)

DEFAULT_MOVESPEED = 0.2
ENTITIES = DotMap(player="player")
MILLISECONDS_PER_FRAME = 80
