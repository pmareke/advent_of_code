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
        range_one = self._create_range(matches.group("x1"), matches.group("x2"))
        range_two = self._create_range(matches.group("y1"), matches.group("y2"))
        return (list(range_one), list(range_two))

    @staticmethod
    def _create_range(start: str, end: str) -> range:
        return range(int(start), int(end) + 1)

    def _lists_overlap(self, first_list: list[int], second_list: list[int]) -> bool:
        if self._is_sublist(first_list, second_list):
            return True
        if self._is_sublist(second_list, first_list):
            return True
        return False

    @staticmethod
    def _is_sublist(left_list: list[int], right_list: list[int]) -> bool:
        if not left_list:
            return True
        if not right_list:
            return False
        return right_list[: len(left_list)] == left_list or Day04._is_sublist(
            left_list, right_list[1:]
        )

    @staticmethod
    def _any_item_in_common(first_list: list[int], second_list: list[int]) -> bool:
        return any(True for x in first_list if x in second_list)
