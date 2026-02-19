import sys
from pathlib import Path

from colorama import Fore


def show_directory_content(
    path: Path, indent: str = "    ", is_root: bool = True
) -> None:
    """Show directory content
    Args:
        path: Path to a directory
        indent: Indentation for directory structure
        is_root: Flag indicating if the path is a root directory.
    Returns:
        A tuple of the total and average salaries.
        If file not found or can't be opened, returns None for both values.
    """
    try:
        if is_root:
            print(f"{Fore.BLUE} {path.name}/")
        for element in path.iterdir():
            if element.is_dir():
                print(f"{indent}{Fore.BLUE} {element.name}/")
                show_directory_content(element, indent + "    ", False)
            else:
                print(f"{indent}{Fore.LIGHTGREEN_EX} {element.name}")
    except FileNotFoundError:
        print("Файл не знайдено")
    except NotADirectoryError:
        print("Шлях не є директорією")


provide_path = Path(sys.argv[1])
show_directory_content(provide_path)
