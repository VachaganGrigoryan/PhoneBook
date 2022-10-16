import logging
import sys
from pathlib import Path

from parser import PhoneBookParser


def key_by_criteria(criteria):
    keys = {"Name": "name", "Surname": "surname", "PhoneNumberCode": "phone"}
    return lambda d: d[keys.get(criteria)]


def run(file_name, sort_type, criteria):
    with open(file_name) as file:
        parser = PhoneBookParser(file)

    if parser.errors:
        print(parser.errors)
    else:
        phone_book = parser.data

        print(sorted(
            phone_book,
            key=key_by_criteria(criteria),
            reverse=sort_type == "Descending"
        ))


if __name__ == '__main__':
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s'
    )

    file_path = input("Enter file path: ")
    while not Path(file_path).exists():
        file_path = input("Enter file path: ")

    sort_type = input("Please choose an ordering to sort: `Ascending` or `Descending`.")
    while sort_type not in ("Ascending", "Descending"):
        sort_type = input("Please choose an ordering to sort: `Ascending` or `Descending`.")

    criteria = input("Please choose criteria: `Name`, `Surname` or `PhoneNumberCode`.")
    while criteria not in ("Name", "Surname", "PhoneNumberCode"):
        criteria = input("Please choose criteria: `Name`, `Surname` or `PhoneNumberCode`.")

    run(file_path, sort_type, criteria)
