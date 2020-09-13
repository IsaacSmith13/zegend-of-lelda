from dotmap import DotMap
import pytmx
from src.utils.get_file_path import get_file_path_from_name, FILE_TYPES


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

            for x, _, global_id in layer:
                if len(layer_data) <= x:
                    layer_data.append([])

                layer_data[x].append(global_id)

        tile_map.append(layer_data)

    level.tile_map = tile_map
    return level
