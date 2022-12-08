from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[int]

    def part_one(self) -> int:
        return sum(line for line in self.lines)

    def part_two(self) -> int:
        seen: set[int] = set()
        total = 0
        while True:
            for line in self.lines:
                total += line
                if total in seen:
                    return total
                seen.add(total)
