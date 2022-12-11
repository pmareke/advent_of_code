from dataclasses import dataclass


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        depth = horizontal = 0
        for line in self.lines:
            op, value = self._parse(line)
            if op == "forward":
                horizontal += value
            if op == "up":
                depth -= value
            if op == "down":
                depth += value
        return depth * horizontal

    def part_two(self) -> int:
        aim = depth = horizontal = 0
        for line in self.lines:
            op, value = self._parse(line)
            if op == "forward":
                horizontal += value
                depth += aim * value
            if op == "up":
                aim -= value
            if op == "down":
                aim += value
        return depth * horizontal

    @staticmethod
    def _parse(line: str) -> tuple[str, int]:
        op, value = line.split(" ")
        return op, int(value)
