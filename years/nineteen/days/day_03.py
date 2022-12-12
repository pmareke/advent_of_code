import re
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Day03:
    lines: list[str]

    def part_one(self) -> int:
        wire_1, wire_2 = self.lines
        wire_1_locations = set(self._solve(wire_1).keys())
        wire_2_locations = set(self._solve(wire_2).keys())
        intersections = wire_1_locations.intersection(wire_2_locations)
        return int(min(abs(x) + abs(y) for (x, y) in intersections))

    def part_two(self) -> int:
        wire_1, wire_2 = self.lines
        wire_1_dict = self._solve(wire_1)
        wire_1_locations = set(wire_1_dict.keys())
        wire_2_dict = self._solve(wire_2)
        wire_2_locations = set(wire_2_dict.keys())
        intersections = wire_1_locations.intersection(wire_2_locations)
        return min(
            [
                wire_1_dict[intersection] + wire_2_dict[intersection]
                for intersection in intersections
            ]
        )

    def _solve(self, wire: str) -> dict[tuple, int]:
        x = y = 0
        seen: dict[tuple, int] = defaultdict(int)
        steps = 1
        for movement in wire.split(","):
            direction, distance = self._parse(movement)
            DX = {"U": -1, "L": 0, "D": 1, "R": 0}
            DY = {"U": 0, "L": -1, "D": 0, "R": 1}
            new_x = new_y = 0
            for d in range(1, distance + 1):
                new_x = x + (DX[direction] * d)
                new_y = y + (DY[direction] * d)
                if (new_x, new_y) not in seen:
                    seen[(new_x, new_y)] = steps
                steps += 1
            x, y = new_x, new_y
        return seen

    @staticmethod
    def _parse(line: str) -> tuple[str, int]:
        regex = re.compile(r"(?P<direction>[L|R|D|U])(?P<distance>\d+)")
        matches = regex.search(line)
        assert matches
        direction = matches.group("direction")
        distance = int(matches.group("distance"))
        return (direction, distance)
