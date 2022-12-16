from dataclasses import dataclass


@dataclass
class Day05:
    lines: list[str]

    def part_one(self) -> int:
        seats: set[int] = set()
        for line in self.lines:
            seats.add(self._parse(line))
        return max(seats)

    def part_two(self) -> int:
        seats: set[int] = set()
        for line in self.lines:
            seats.add(self._parse(line))
        for seat in sorted(seats):
            if seat + 1 not in seats and seat + 2 in seats:
                return seat + 1
        return 0

    @staticmethod
    def _parse(line: str) -> int:
        number = ""
        for letter in line:
            number += "1" if letter in ["B", "R"] else "0"
        row = int(number[:7], 2)
        column = int(number[7:], 2)
        return row * 8 + column
