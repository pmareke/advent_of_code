import hashlib
from dataclasses import dataclass


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        return self._solve(self.lines[0], number_of_zeros=5)

    def part_two(self) -> int:
        return self._solve(self.lines[0], number_of_zeros=6)

    @staticmethod
    def _solve(secret_key: str, number_of_zeros: int) -> int:
        number = 0
        while True:
            md5 = hashlib.md5(f"{secret_key}{number}".encode())
            if md5.hexdigest().startswith("0" * number_of_zeros):
                return number
            number += 1
