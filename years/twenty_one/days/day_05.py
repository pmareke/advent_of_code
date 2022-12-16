from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Day05:
    lines: list[str]

    def part_one(self) -> int:
        seen: dict[tuple, int] = defaultdict(int)
        for line in self.lines:
            x, y = line.split(" -> ")
            x1, y1 = map(int, x.split(","))
            x2, y2 = map(int, y.split(","))
            if x1 != x2 and y1 != y2:
                continue
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            for xx in range(0, dx + 1):
                for yy in range(0, dy + 1):
                    new_x = x1 + xx * (1 if x1 < x2 else -1)
                    new_y = y1 + yy * (1 if y1 < y2 else -1)
                    new_point = (new_x, new_y)
                    seen[new_point] += 1
        return len(dict(filter(lambda point: point[1] >= 2, seen.items())))

    def part_two(self) -> int:
        seen: dict[tuple, int] = defaultdict(int)
        for line in self.lines:
            x, y = line.split(" -> ")
            x1, y1 = map(int, x.split(","))
            x2, y2 = map(int, y.split(","))
            if x1 != x2 and y1 != y2:
                if x1 == y1 and x2 == y2:
                    for idx in range(min(x1, x2), max(x1, x2) + 1):
                        new_point = (idx, idx)
                        seen[new_point] += 1
                    continue
                if x1 == y2 and x2 == y1:
                    for idx in range(abs(x1 - y1) + 1):
                        new_x = x1 + idx * (1 if x1 < x2 else -1)
                        new_y = y1 + idx * (1 if y1 < y2 else -1)
                        new_point = (new_x, new_y)
                        seen[new_point] += 1
                    continue
                for idx in range(abs(x1 - x2) + 1):
                    new_x = x1 + idx * (1 if x1 < x2 else -1)
                    new_y = y1 + idx * (1 if y1 < y2 else -1)
                    new_point = (new_x, new_y)
                    seen[new_point] += 1
                continue
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            for xx in range(0, dx + 1):
                for yy in range(0, dy + 1):
                    new_x = x1 + xx * (1 if x1 < x2 else -1)
                    new_y = y1 + yy * (1 if y1 < y2 else -1)
                    new_point = (new_x, new_y)
                    seen[new_point] += 1
        return len(dict(filter(lambda point: point[1] >= 2, seen.items())))
