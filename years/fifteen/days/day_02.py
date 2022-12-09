import re
from dataclasses import dataclass


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        result = 0
        for line in self.lines:
            (length, width, height) = self._parse_line(line)
            perimeters = [length * width, width * height, height * length]
            result += sum(2 * perimeter for perimeter in perimeters) + min(perimeters)
        return result

    def part_two(self) -> int:
        result = 0
        for line in self.lines:
            (length, width, height) = self._parse_line(line)
            sizes = sorted([length, width, height])
            result += 2 * sizes[0] + 2 * sizes[1] + (length * width * height)
        return result

    @staticmethod
    def _parse_line(line: str) -> tuple[int, int, int]:
        regex = re.compile(r"(?P<length>\d*)x(?P<width>\d+)x(?P<height>\d+)")
        matches = regex.search(line)
        assert matches
        length = int(matches.group("length"))
        width = int(matches.group("width"))
        height = int(matches.group("height"))
        return (length, width, height)
