from dataclasses import dataclass
from typing import Callable


@dataclass
class Day03:
    lines: list[str]

    def part_one(self) -> int:
        gamma = ""
        epsilon = ""
        most_common = self._find_most_common(self.lines)
        for value in most_common:
            gamma += "1" if value == "1" else "0"
            epsilon += "0" if value == "1" else "1"
        return int(gamma, 2) * int(epsilon, 2)

    def part_two(self) -> int:
        oxygen = self._find_number(self.lines, 0, lambda x, y: x == y)
        co2 = self._find_number(self.lines, 0, lambda x, y: x != y)
        return int(co2, 2) * int(oxygen, 2)

    def _find_number(self, lines: list[str], start: int, callback: Callable) -> str:
        if len(lines) == 1:
            return lines[0]
        most_common = self._find_most_common(lines)
        numbers = [
            number for number in lines if callback(number[start], most_common[start])
        ]
        return self._find_number(numbers, start + 1, callback)

    def _find_most_common(self, lines: list[str]) -> list[str]:
        digits: list[int] = [0 for _ in range(len(self.lines[0]))]
        for idx in range(len(lines[0])):
            for line in lines:
                digits[idx] += int(line[idx])
        return [
            "0" if len(lines) - digit > len(lines) // 2 else "1" for digit in digits
        ]
