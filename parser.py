from dataclasses import dataclass
from typing import List


@dataclass
class PhoneBookValidationError:
    line: int
    msgs: List

    def __str__(self):
        return f'line {self.line}: {"".join(self.msgs)}'


class PhoneBookParser:

    def __init__(self, file):
        self.errors = []
        self.file_content = file.readlines()
        self.data = []
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

            full_name, phone = row

            if len(phone.strip()) != 9:
                self.errors.append(PhoneBookValidationError(
                    line=n,
                    msgs=["Phone number should be with 9 digits."]
                ))
                continue

            name, surname = full_name.strip().split()

            self.data.append({
                'name': name,
                'surname': surname,
                'phone': phone
            })
