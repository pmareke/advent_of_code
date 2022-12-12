from dataclasses import dataclass


@dataclass
class Day03:
    lines: list[str]

    def part_one(self) -> int:
        return self._solve(down=1, right=3)

    def part_two(self) -> int:
        result = 1
        for down, right in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
            result *= self._solve(down, right)
        return result

    def _solve(self, down: int, right: int) -> int:
        result = 0
        x = y = 0
        while x < len(self.lines):
            if self.lines[x][y] == "#":
                result += 1
            x += down
            y = (y + right) % len(self.lines[0])
        return result
