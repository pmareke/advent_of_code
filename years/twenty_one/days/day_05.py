from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Day05:
    lines: list[str]

    def part_one(self) -> int:
        seen: dict[tuple, int] = defaultdict(int)
        for line in self.lines:
            point_1, point_2 = line.split(" -> ")
            x1, y1 = map(int, point_1.split(","))
            x2, y2 = map(int, point_2.split(","))
            dx = x2 - x1
            dy = y2 - y1
            diff: int = max(abs(dx), abs(dy))
            for idx in range(diff + 1):
                x = x1 + (1 if dx > 0 else (-1 if dx < 0 else 0)) * idx
                y = y1 + (1 if dy > 0 else (-1 if dy < 0 else 0)) * idx
                if dx == 0 or dy == 0:
                    seen[(x, y)] += 1
        return len([point for point in seen if seen[point] > 1])

    def part_two(self) -> int:
        seen: dict[tuple, int] = defaultdict(int)
        for line in self.lines:
            point_x, point_y = line.split(" -> ")
            x1, y1 = map(int, point_x.split(","))
            x2, y2 = map(int, point_y.split(","))
            dx = x2 - x1
            dy = y2 - y1
            diff: int = max(abs(dx), abs(dy))
            for idx in range(diff + 1):
                x = x1 + (1 if dx > 0 else (-1 if dx < 0 else 0)) * idx
                y = y1 + (1 if dy > 0 else (-1 if dy < 0 else 0)) * idx
                seen[(x, y)] += 1
        return len([point for point in seen if seen[point] > 1])
