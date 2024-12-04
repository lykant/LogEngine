import pathlib
import os

# Constants
DEFAULT_SEP = "-"


def create_dir(dir: str) -> str:
    if not os.path.exists(dir):
        os.mkdir(dir)
    return dir


def make_file_name(list_word: list, file_ext: str, sep: str = DEFAULT_SEP) -> str:
    file_ext = f".{file_ext}" if not ("." in file_ext) else file_ext
    file_name = sep.join([str(a).strip() for a in list_word]) + f"{file_ext}"
    return file_name


def make_full_dir(base_dir: str, current_dir: str) -> str:
    full_dir = create_dir(os.path.join(base_dir, current_dir))
    return full_dir


def make_full_path(full_dir: str, file_name: str) -> str:
    create_dir(full_dir)
    full_path = os.path.join(full_dir, file_name)
    if os.path.exists(full_path):
        os.remove(full_path)
    return full_path


def take_dir_name(file_path: pathlib.Path) -> str:
    return os.path.dirname(file_path)
