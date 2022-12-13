from dataclasses import dataclass


@dataclass
class Day03:
    lines: list[str]

    def part_one(self) -> int:
        directions = self.lines[0]
        x = y = 0
        seen: set[tuple] = set()
        seen.add((x, y))
        for direction in directions:
            (x, y) = self._update_position(direction, x, y)
            seen.add((x, y))
        return len(seen)

    def part_two(self) -> int:
        directions = self.lines[0]
        x = x1 = y = y1 = 0
        seen: set[tuple] = set()
        seen.add((x, y))
        for index in range(0, len(directions), 2):
            (x, y) = self._update_position(directions[index], x, y)
            (x1, y1) = self._update_position(directions[index + 1], x1, y1)
            seen.add((x, y))
            seen.add((x1, y1))
        return len(seen)

    @staticmethod
    def _update_position(direction: str, x: int, y: int) -> tuple[int, int]:
        if direction == "^":
            return (x + 1, y)
        if direction == "v":
            return (x - 1, y)
        if direction == ">":
            return (x, y + 1)
        return (x, y - 1)
