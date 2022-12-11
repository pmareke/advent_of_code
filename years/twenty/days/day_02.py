import re
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        return sum(1 for line in self.lines if self._is_valid(line))

    def part_two(self) -> int:
        return sum(1 for line in self.lines if self._is_valid_2(line))

    def _is_valid(self, line: str) -> bool:
        minimum, maximum, letter, password = self._parse(line)
        letters: dict[str, int] = defaultdict(int)
        for character in password:
            letters[character] += 1
        return letters[letter] >= minimum and letters[letter] <= maximum

    def _is_valid_2(self, line: str) -> bool:
        pos_one, pos_two, letter, password = self._parse(line)
        valid_one = password[pos_one - 1] == letter and password[pos_two - 1] != letter
        valid_two = password[pos_one - 1] != letter and password[pos_two - 1] == letter
        return valid_one or valid_two

    @staticmethod
    def _parse(line: str) -> tuple[int, int, str, str]:
        regex = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<pass>\w+)")
        matches = regex.search(line)
        assert matches
        minimum = int(matches.group("min"))
        maximum = int(matches.group("max"))
        letter = matches.group("letter")
        password = matches.group("pass")
        return (minimum, maximum, letter, password)
