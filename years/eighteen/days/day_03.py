import re
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Day03:
    lines: list[str]

    def part_one(self) -> int:
        claims: dict[str, int] = defaultdict(int)
        for line in self.lines:
            _, left, up, wide, tall = self._parse(line)
            for idx in range(up, up + tall):
                for idy in range(left, left + wide):
                    claims[f"{idx},{idy}"] += 1
        return sum(1 for claim in claims.values() if claim > 1)

    def part_two(self) -> int:
        claims: dict[str, int] = defaultdict(int)
        boxes: dict[int, list[tuple]] = defaultdict(list)
        for line in self.lines:
            box_id, left, up, wide, tall = self._parse(line)
            box: list[tuple] = []
            for idx in range(up, up + tall):
                for idy in range(left, left + wide):
                    box.append((idx, idy))
                    claims[f"{idx},{idy}"] += 1
            boxes[box_id] = box
        for box_id, box in boxes.items():
            if all(claims[f"{pair[0]},{pair[1]}"] == 1 for pair in box):
                return box_id
        return 0

    @staticmethod
    def _parse(line: str) -> tuple[int, int, int, int, int]:
        regex = re.compile(
            r"#(?P<id>\d+) @ (?P<left>\d+),(?P<up>\d+): (?P<wide>\d+)x(?P<tall>\d+)"
        )
        matches = regex.search(line)
        assert matches
        box_id = int(matches.group("id"))
        left = int(matches.group("left"))
        up = int(matches.group("up"))
        wide = int(matches.group("wide"))
        tall = int(matches.group("tall"))
        return (box_id, left, up, wide, tall)
