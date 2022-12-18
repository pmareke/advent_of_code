from dataclasses import dataclass


@dataclass
class Day05:
    lines: list[str]

    def part_one(self) -> int:
        numbers = list(map(int, self.lines))
        size = len(numbers)
        limit = 0
        steps = 0
        while limit < size:
            steps += 1
            numbers[limit] += 1
            limit += numbers[limit] - 1
        return steps

    def part_two(self) -> int:
        numbers = list(map(int, self.lines))
        size = len(numbers)
        limit = 0
        steps = 0
        while limit < size:
            steps += 1
            offset = -1 if numbers[limit] >= 3 else 1
            numbers[limit] += offset
            limit += numbers[limit] - offset
        print(numbers)
        return steps
