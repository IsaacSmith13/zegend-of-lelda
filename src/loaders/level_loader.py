from dotmap import DotMap
import pytmx
from src.utils.get_file_path import get_file_path_from_name, FILE_TYPES
from src.objects.terrain.tile import Tile


def load_level(name):
    data = pytmx.load_pygame(get_file_path_from_name(name, FILE_TYPES.level), pixelalpha=True)

    level = DotMap(
        data=data,
        level_height=data.height * data.tileheight,
        level_width=data.width * data.tilewidth,
        tile_height=data.tileheight,
        tile_width=data.tilewidth
    )

    tile_map = []

    for layer in data.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            layer_data = []

            for x, y, global_id in layer:
                if len(layer_data) <= x:
                    layer_data.append([])

                properties = data.get_tile_properties_by_gid(global_id)
                layer_data[x].append(Tile(
                    collidable=bool(properties and properties["collidable"]),
                    image=data.get_tile_image_by_gid(global_id),
                    x=x,
                    y=y
                ))

        tile_map.append(layer_data)

    level.tile_map = tile_map
    return level
