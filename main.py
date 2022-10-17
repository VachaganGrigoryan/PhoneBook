from pathlib import Path

from parser import PhoneBookParser


def key_by_criteria(criteria):
    if criteria == "PhoneNumberCode":
        return lambda d: d["phone"][:3]

    keys = {"Name": "name", "Surname": "surname"}
    return lambda d: d[keys.get(criteria)]


def run(file_name_or_path, order, criteria):
    parser = PhoneBookParser(file_name_or_path)

    if parser.errors:
        print('\nValidation:')
        for err in parser.errors:
            print(err)
    else:
        print('\nPhone Book:')
        for line in sorted(
            parser.data,
            key=key_by_criteria(criteria),
            reverse=order == "Descending"
        ):
            print(' '.join(line.values()))


if __name__ == '__main__':

    file_path = input("Enter file path: ")
    while not Path(file_path).exists():
        file_path = input("Enter file path: ")

    order = input("Please choose an ordering to sort: `Ascending` or `Descending`. ")
    while order not in ("Ascending", "Descending"):
        order = input("Please choose an ordering to sort: `Ascending` or `Descending`. ")

    criteria = input("Please choose criteria: `Name`, `Surname` or `PhoneNumberCode`. ")
    while criteria not in ("Name", "Surname", "PhoneNumberCode"):
        criteria = input("Please choose criteria: `Name`, `Surname` or `PhoneNumberCode`. ")

    run(file_path, order, criteria)
