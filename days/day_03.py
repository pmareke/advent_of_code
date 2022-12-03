import string
from dataclasses import dataclass


@dataclass
class Day03:
    lines: list[str]

    def part_one(self) -> int:
        duplicates: list[str] = []
        for line in self.lines:
            duplicate = self._find_duplicate_in_line(line)
            duplicates.append(duplicate)
        return self._calculate_priorities(duplicates)

    def part_two(self) -> int:
        step = 3
        duplicates: list[str] = []
        for index in range(0, len(self.lines), step):
            lines = self.lines[index : index + step]
            duplicate = self._find_duplicate_in_groups_of_three_lines(lines)
            duplicates.append(duplicate)
        return self._calculate_priorities(duplicates)

    @staticmethod
    def _find_duplicate_in_line(line: str) -> str:
        medium = len(line) // 2
        duplicates = set(line[:medium]) & set(line[medium:])
        return list(duplicates)[0]

    @staticmethod
    def _find_duplicate_in_groups_of_three_lines(lines: list[str]) -> str:
        duplicates = set(lines[0]) & set(lines[1]) & set(lines[2])
        return list(duplicates)[0]

    @staticmethod
    def _calculate_priorities(duplicates: list[str]) -> int:
        return sum(
            string.ascii_letters.index(duplicate) + 1 for duplicate in duplicates
        )
