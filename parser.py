from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


@dataclass
class PhoneBookValidationError:
    line: int
    msgs: List

    def __str__(self):
        return f'line {self.line}: {"".join(self.msgs)}'


def walk(path: str):
    entries = Path(path)
    if entries.is_file():
        yield entries
    else:
        for entry in entries.iterdir():
            if entry.is_dir():
                walk(f'{path}/{entry.name}')
            yield entry


class PhoneBookParser:

    def __init__(self, path: str, file_types: Tuple = None):
        self.file_types = file_types or ('txt',)
        self.file_content = []
        self.errors = []
        self.data = []
        print('\nFile Structure:')

        for file_path in walk(path):
            if file_path.name.split('.')[-1] in self.file_types:
                with open(file_path) as file:
                    self.parse(file)

    def parse(self, file):
        self.file_content = file.readlines()
        print(''.join(self.file_content))

        for n, line in enumerate(self.file_content, start=1):
            row = line.split('-')
            if len(row) != 2:
                row = line.split(':')
                if len(row) != 2:
                    self.errors.append(PhoneBookValidationError(
                        line=n,
                        msgs=["The separator should be `:` or `-`."]
                    ))
                    continue

            full_name, phone = row[0].strip(), row[1].strip()

            if len(phone) != 9:
                self.errors.append(PhoneBookValidationError(
                    line=n,
                    msgs=["Phone number should be with 9 digits."]
                ))
                continue

            try:
                name, surname = full_name.split()
            except:
                name, surname = full_name, ''

            self.data.append({
                'name': name,
                'surname': surname,
                'phone': phone
            })
