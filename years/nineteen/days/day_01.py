from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[int]

    def part_one(self) -> int:
        return sum(int(line / 3) - 2 for line in self.lines)

    def part_two(self) -> int:
        return sum(self._calculate_fuel(line) for line in self.lines)

    def _calculate_fuel(self, mass: int) -> int:
        fuel = int(mass / 3) - 2
        return fuel + self._calculate_fuel(fuel) if fuel > 0 else 0
