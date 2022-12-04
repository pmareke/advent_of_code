import re
from dataclasses import dataclass


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        overlap = 0
        for line in self.lines:
            first_list, second_list = self._parse_line(line)
            if self._lists_overlap(first_list, second_list):
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
        regex = re.compile(r"(?P<x1>\d+)-(?P<x2>\d+),(?P<y1>\d+)-(?P<y2>\d+)")
        matches = regex.search(line)
        assert matches
        first_list = self._create_list(matches.group("x1"), matches.group("x2"))
        second_list = self._create_list(matches.group("y1"), matches.group("y2"))
        return (first_list, second_list)

    @staticmethod
    def _create_list(start: str, end: str) -> list[int]:
        return list(range(int(start), int(end) + 1))

    def _lists_overlap(self, first_list: list[int], second_list: list[int]) -> bool:
        if self._is_subset(first_list, second_list):
            return True
        if self._is_subset(second_list, first_list):
            return True
        return False

    def _is_subset(self, left_list: list[int], right_list: list[int]) -> bool:
        left_set = set(left_list)
        right_set = set(right_list)
        return left_set.issubset(right_set) or right_set.issubset(left_set)

    @staticmethod
    def _any_item_in_common(first_list: list[int], second_list: list[int]) -> bool:
        return any(True for x in first_list if x in second_list)
