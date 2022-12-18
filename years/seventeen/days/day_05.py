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
            previous = limit
            limit += numbers[limit]
            numbers[previous] += 1
        return steps

    def part_two(self) -> int:
        numbers = list(map(int, self.lines))
        size = len(numbers)
        limit = 0
        steps = 0
        while limit < size:
            steps += 1
            previous = limit
            limit += numbers[limit]
            numbers[previous] += -1 if numbers[previous] >= 3 else 1
        print(numbers)
        return steps
