from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[str]

    def part_one(self) -> int:
        return self._calculate_increases(step=1)

    def part_two(self) -> int:
        return self._calculate_increases(step=3)

    def _calculate_increases(self, step: int) -> int:
        increases = 0
        for index, line in enumerate(self.lines):
            if index == len(self.lines) - step:
                break
            if int(line) < int(self.lines[index + step]):
                increases += 1
        return increases
