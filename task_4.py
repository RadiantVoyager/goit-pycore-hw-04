from typing import Callable, Dict

from colorama import Fore
from rich.console import Console
from rich.table import Table


def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def say_to_hello():
    return f"{Fore.YELLOW} How can I help you?"


def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return f"\n{Fore.GREEN} Contact added."
    else:
        return f"\n{Fore.RED} Contact already exists."


def change_phone(args: list, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"\n{Fore.GREEN} Phone number changed."
    else:
        return f"\n{Fore.RED} There is no such a contact"


def show_phone(args: list, contacts: dict) -> str:
    name = args[0]
    if name in contacts:
        return f"\n{Fore.GREEN} {contacts[name]}"
    else:
        return f"\n{Fore.RED} There is no such a contact"


def show_all(contacts: dict) -> Table:
    table = Table(title="\nContacts", style="cyan")
    table.add_column("Name", style="magenta")
    table.add_column("Phone number", style="green")
    for name, phone in contacts.items():
        table.add_row(name, phone)
    return table


def main():
    """
    The assistant bot
    """
    contacts = {}
    console = Console()
    commands: Dict[str, Callable] = {
        "hello": say_to_hello,
        "add": add_contact,
        "change": change_phone,
        "phone": show_phone,
        "all": show_all,
    }
    COMMANDS_DESCRIPTION = """
    Commands for the bot:
    hello -> get the question
    add <contact name> <phone number> -> add a new contact name and number
    change <contact name> <phone number> -> change existing contact's phone number
    phone <contact name> -> get existing contact's phone number
    all -> get all existing contact's phone numbers
    close or exit -> close the bot
    """
    print(f"\n{Fore.YELLOW} Welcome to the assistant bot! \n{COMMANDS_DESCRIPTION}")
    while True:
        try:
            user_input = input(f"\n{Fore.WHITE} Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(f"\n{Fore.GREEN} Good bye!\n")
                break
            elif command in commands:
                result = commands[command](args, contacts)
                console.print(result)
            else:
                print(f"\n{Fore.RED} Invalid command.")
        except ValueError:
            print(f"\n{Fore.RED}Invalid input. Please try again")


if __name__ == "__main__":
    main()
