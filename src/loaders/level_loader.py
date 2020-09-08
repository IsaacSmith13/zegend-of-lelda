from dotmap import DotMap
import pytmx
from src.utils.get_file_path import get_file_path_from_name, FILE_TYPES


def load_level(name):
    data = pytmx.load_pygame(get_file_path_from_name(name, FILE_TYPES.level), pixelalpha=True)

    level = DotMap(
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
                tile_asset = data.get_tile_image_by_gid(global_id)

                if tile_asset:
                    layer_data.append(DotMap(
                        asset=tile_asset,
                        global_id=global_id,
                        x=x * data.tilewidth,
                        y=y * data.tileheight
                    ))

            tile_map.append(layer_data)

    level.tile_map = tile_map
    return level
