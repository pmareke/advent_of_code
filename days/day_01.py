import pytest
from dataclasses import dataclass
from expects import equal, expect
from typing import List


@dataclass
class Day01:
    lines: List[str]

    def part_one(self) -> int:
        return max(self._calculate_calories())

    def part_two(self) -> int:
        sorted_calories = sorted(self._calculate_calories(), reverse=True)
        print(sorted_calories)
        return sum(sorted_calories[:3])

    def _calculate_calories(self) -> List[int]:
        calories: List[int] = []
        acc = 0
        for line in self.lines:
            if line == "\n":
                calories.append(acc)
                acc = 0
                continue
            acc += int(line)
        return calories
