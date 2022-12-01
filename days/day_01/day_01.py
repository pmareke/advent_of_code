from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[str]

    def part_one(self) -> int:
        return max(self._calculate_calories())

    def part_two(self) -> int:
        sorted_calories = sorted(self._calculate_calories(), reverse=True)
        return sum(sorted_calories[:3])

    def _calculate_calories(self) -> list[int]:
        calories: list[int] = []
        for elf in "\n".join(self.lines).split("\n\n"):
            print(elf)
            more_calories = sum(int(line) for line in elf.split("\n"))
            calories.append(more_calories)
        return calories
