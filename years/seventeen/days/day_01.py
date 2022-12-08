from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[str]

    def part_one(self) -> int:
        return self._calculate_catcha(step=1)

    def part_two(self) -> int:
        step = len(self.lines[0]) // 2
        return self._calculate_catcha(step=step)

    def _calculate_catcha(self, step: int) -> int:
        numbers: list[int] = []
        for index, digit in enumerate(self.lines[0]):
            input_length = len(self.lines[0])
            next_index = (index + step) % input_length
            if digit == self.lines[0][next_index]:
                numbers.append(int(digit))
        return sum(numbers)
