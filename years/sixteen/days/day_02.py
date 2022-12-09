from dataclasses import dataclass
from typing import Union


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        pad: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result: list[str] = []
        x = y = 1
        for line in self.lines:
            for digit in line:
                if digit == "U" and x > 0:
                    x += -1
                if digit == "D" and x < 2:
                    x += 1
                if digit == "L" and y > 0:
                    y += -1
                if digit == "R" and y < 2:
                    y += 1
            result.append(str(pad[x][y]))
        return int("".join(result))

    def part_two(self) -> str:
        pad: list[list[Union[str, int]]] = [
            [0, 0, 1, 0, 0],
            [0, 2, 3, 4, 0],
            [5, 6, 7, 8, 9],
            [0, "A", "B", "C", 0],
            [0, 0, "D", 0, 0],
        ]
        result: list[str] = []
        x = 2
        y = 0
        for line in self.lines:
            for digit in line:
                if digit == "U" and x > 0 and pad[x - 1][y] != 0:
                    x += -1
                if digit == "D" and x < 4 and pad[x + 1][y] != 0:
                    x += 1
                if digit == "L" and y > 0 and pad[x][y - 1] != 0:
                    y += -1
                if digit == "R" and y < 4 and pad[x][y + 1] != 0:
                    y += 1
            result.append(str(pad[x][y]))
        return "".join(result)
