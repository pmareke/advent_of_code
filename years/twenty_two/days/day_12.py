from collections import deque
from dataclasses import dataclass
from typing import Deque


@dataclass
class Day12:
    lines: list[str]

    def part_one(self) -> int:
        area, queue = self._parse()
        return self._breadth_first_search(area, queue)

    def part_two(self) -> int:
        area, queue = self._parse(part_two=True)
        return self._breadth_first_search(area, queue)

    def _parse(self, part_two: bool = False) -> tuple[list[list[int]], Deque]:
        area: list[list[int]] = []
        starts: list[list[int]] = []
        for idx, line in enumerate(self.lines):
            area.append([])
            for idy, position in enumerate(line):
                desired_position = "a" if part_two else "S"
                if position == desired_position:
                    starts.append([idx, idy])
                    area[idx].append(1)
                    continue
                if position == "E":
                    area[idx].append(26)
                    continue
                area[idx].append(ord(position) - ord("a") + 1)
        queue: Deque = deque()
        for start in starts:
            queue.append(((start[0], start[1]), 0))
        return (area, queue)

    @staticmethod
    def _breadth_first_search(area: list[list[int]], queue: Deque) -> int:
        rows = len(area)
        columns = len(area[0])
        seen = set()
        while queue:
            point, distance = queue.popleft()
            if point in seen:
                continue
            seen.add(point)
            point_x, point_y = point
            if area[point_x][point_y] == 26:
                return int(distance + 1)
            couples: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for idx, idy in couples:
                next_row = idx + point_x
                next_column = idy + point_y
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and area[next_row][next_column] <= area[point_x][point_y] + 1
                ):
                    next_point = (next_row, next_column)
                    queue.append((next_point, distance + 1))
        return 0
