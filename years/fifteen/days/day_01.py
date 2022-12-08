from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[str]

    def part_one(self) -> int:
        result = 0
        for digit in self.lines[0]:
            result += 1 if digit == "(" else -1
        return result

    def part_two(self) -> int:
        result = 0
        for index, digit in enumerate(self.lines[0]):
            result += 1 if digit == "(" else -1
            if result == -1:
                return index + 1
        return result
