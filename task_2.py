def get_cats_info(path: str) -> list | None:
    """Get id, name, age of the provided cats info.
    Args:
        path: Path to a file with cats data.
    Returns:
        A list of dictionaries with cat information.
        If file not found or can't be opened or input format isn't correct,
        returns None.
    """
    try:
        cats_info = []
        with open(path, encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")
                cats_info.append({"id": cat_id, "name": name, "age": age})
        return cats_info
    except FileNotFoundError:
        print("Файл не знайдено")
        return None
    except UnicodeDecodeError:
        print("Файл не може бути відкрито - не правильне кодування")
        return None
    except ValueError:
        print("He правильний формат даних")
        return None


cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
