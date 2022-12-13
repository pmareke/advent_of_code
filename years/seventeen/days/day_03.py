import math
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Day03:
    number: int

    def part_one(self) -> int:
        # Taking a look to the grid, the right bottom corner is always an odd
        # square, e.g. 3², 5², ...(2*layer - 1)²
        # So the layer of the closest odd square to the target is
        # layer = (math.sqrt(target) + 1) / 2
        layers = math.ceil(math.sqrt(self.number))
        y_distance = math.ceil((layers + 1) / 2)
        x_distance = abs(y_distance - (self.number % layers))
        return y_distance + x_distance - 1

    def part_two(self) -> int:
        x, y = 0, 0
        grid: dict[tuple[int, int], int] = defaultdict(int)
        grid[(0, 0)] = 1
        while grid[(x, y)] <= self.number:
            x, y = self._neighbour(x, y)
            neighbours = []
            DX = [-1, 0, 1]
            DY = [0, 1, -1]
            for dx in DX:
                for dy in DY:
                    neighbours.append(grid[x + dx, y + dy])
            grid[(x, y)] = sum(neighbours)
        return grid[(x, y)]

    def _neighbour(self, x: int, y: int) -> tuple[int, int]:
        if x == y == 0:
            return (1, 0)
        if y > -x and x > y:
            return (x, y + 1)
        if y > -x and y >= x:
            return (x - 1, y)
        if y <= -x and x < y:
            return (x, y - 1)
        return (x + 1, y)
