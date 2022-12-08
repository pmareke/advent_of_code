from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[str]

    def part_one(self) -> int:
        return self._calculate_sorted_calories()[0]

    def part_two(self) -> int:
        return sum(self._calculate_sorted_calories()[:3])

    def _calculate_sorted_calories(self) -> list[int]:
        calories: list[int] = []
        for elf in "\n".join(self.lines).split("\n\n"):
            more_calories = sum(int(line) for line in elf.split("\n"))
            calories.append(more_calories)
        return sorted(calories, reverse=True)
