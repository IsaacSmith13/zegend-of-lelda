import os
from dotmap import DotMap
from definitions import ROOT_PATH


FILE_TYPES = DotMap(
    audio=DotMap(extension=".ogg", path="audio"),
    level=DotMap(extension=".tmx", path="levels")
)


def get_file_path_from_name(name, file_type):
    if file_type not in FILE_TYPES.values():
        raise ValueError(f'Attempted to use file type {file_type} which is invalid')

    return os.path.join(
        ROOT_PATH,
        "src/assets",
        file_type.path,
        name.lower().replace(" ", "_") + file_type.extension
    )
