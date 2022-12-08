import re
from dataclasses import dataclass


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        overlap = 0
        for line in self.lines:
            first_list, second_list = self._parse_line(line)
            if self._are_subset(first_list, second_list):
                overlap += 1
        return overlap

    def part_two(self) -> int:
        overlap = 0
        for line in self.lines:
            first_list, second_list = self._parse_line(line)
            if self._any_item_in_common(first_list, second_list):
                overlap += 1
        return overlap

    def _parse_line(self, line: str) -> tuple[list[int], list[int]]:
        regex = re.compile(r"(?P<s1>\d+)-(?P<e1>\d+),(?P<s2>\d+)-(?P<e2>\d+)")
        matches = regex.search(line)
        assert matches
        first_list = self._create_list(matches.group("s1"), matches.group("e1"))
        second_list = self._create_list(matches.group("s2"), matches.group("e2"))
        return (first_list, second_list)

    @staticmethod
    def _create_list(start: str, end: str) -> list[int]:
        return list(range(int(start), int(end) + 1))

    def _are_subset(self, left_list: list[int], right_list: list[int]) -> bool:
        left_set = set(left_list)
        right_set = set(right_list)
        return left_set.issubset(right_set) or right_set.issubset(left_set)

    @staticmethod
    def _any_item_in_common(first_list: list[int], second_list: list[int]) -> bool:
        return len(set(first_list).intersection(set(second_list))) > 0
