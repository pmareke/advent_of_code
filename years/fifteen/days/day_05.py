import re
from dataclasses import dataclass


@dataclass
class Day05:
    lines: list[str]

    def part_one(self) -> int:
        return sum(1 for line in self.lines if self._is_valid(line))

    def part_two(self) -> int:
        return sum(1 for line in self.lines if self._is_valid_part_two(line))

    def _is_valid(self, line: str) -> bool:
        if self._has_invalid_letters(line):
            return False
        if not self._has_three_vocals(line):
            return False
        if not self._has_two_letters_in_a_row(line):
            return False
        return True

    @staticmethod
    def _has_three_vocals(line: str) -> bool:
        return len(re.findall(r"[aeiou]", line)) >= 3

    @staticmethod
    def _has_two_letters_in_a_row(line: str) -> bool:
        for idx, letter in enumerate(line):
            if idx == len(line) - 1:
                break
            if letter == line[idx + 1]:
                return True
        return False

    @staticmethod
    def _has_invalid_letters(line: str) -> bool:
        for invalid in ["ab", "cd", "pq", "xy"]:
            if invalid in line:
                return True
        return False

    def _is_valid_part_two(self, line: str) -> bool:
        if not self._has_pair_of_letters(line):
            return False
        if not self._has_one_letter_repeated_with_one_letter_in_between(line):
            return False
        return True

    @staticmethod
    def _has_pair_of_letters(line: str) -> bool:
        for idx in range(len(line) - 3):
            pair = line[idx : idx + 2]
            if pair in line[idx + 2 :]:
                return True
        return False

    @staticmethod
    def _has_one_letter_repeated_with_one_letter_in_between(line: str) -> bool:
        for idx in range(len(line) - 2):
            if line[idx] == line[idx + 2]:
                return True
        return False
