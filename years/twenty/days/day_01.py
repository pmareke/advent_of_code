from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[int]

    def part_one(self) -> int:
        for line in self.lines:
            for another_line in self.lines[1:]:
                if line + another_line == 2020:
                    return line * another_line
        return 0

    def part_two(self) -> int:
        for line in self.lines:
            for another_line in self.lines[1:]:
                for extra_line in self.lines[2:]:
                    if line + another_line + extra_line == 2020:
                        return line * another_line * extra_line
        return 0
