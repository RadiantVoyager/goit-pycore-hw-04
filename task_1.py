def total_salary(path: str) -> tuple[int, int] | tuple[None, None]:
    """Calculate total and average salaries.
    Args:
        path: Path to a file with data.
    Returns:
        A tuple of the total and average salaries.
        If file not found or can't be opened or input format isn't correct,
        returns None for both values.
    """
    try:
        with open(path, encoding="utf-8") as file:
            salaries = [int(line.split(",")[1]) for line in file]
        total_salary = sum(salaries)
        average_salary = int(total_salary / len(salaries))
        return total_salary, average_salary
    except FileNotFoundError:
        print("Файл не знайдено")
        return None, None
    except UnicodeDecodeError:
        print("Файл не може бути відкрито - не правильне кодування")
        return None, None
    except ValueError:
        print("He правильний формат даних")
        return None, None


total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
