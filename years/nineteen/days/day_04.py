import re
from dataclasses import dataclass


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        result = 0
        start, end = map(int, self.lines[0].split("-"))
        for secret in range(start, end + 1):
            if self._is_valid(secret):
                result += 1
        return result

    def part_two(self) -> int:
        result = 0
        start, end = map(int, self.lines[0].split("-"))
        for secret in range(start, end + 1):
            if self._is_valid_part_two(secret):
                result += 1
        return result

    @staticmethod
    def _is_valid(secret: int) -> bool:
        password = f"{secret}"
        if any(int(i) > int(j) for i, j in zip(password, password[1:])):
            return False
        return bool(re.search(r"(\d)\1", password))

    @staticmethod
    def _is_valid_part_two(secret: int) -> bool:
        password = f"{secret}"
        if any(int(i) > int(j) for i, j in zip(password, password[1:])):
            return False
        return any([len(x[0]) == 2 for x in re.findall(r"((\d)\2+)", password)])
