import re
from dataclasses import dataclass


@dataclass
class Day10:
    lines: list[str]

    def part_one(self) -> int:
        cycles = self._calculate_cycles()
        first, last, step = 19, 220, 40
        return sum((idx + 1) * cycles[idx] for idx in range(first, last, step))

    def part_two(self) -> list[str]:
        crt_high, crt_wide = 6, 40
        crt_display: list[list[str]] = [[] for _ in range(crt_high)]
        cycles = self._calculate_cycles()
        for idx in range(crt_high):
            for idy in range(crt_wide):
                cycle = (idx * crt_wide) + idy
                value = "#" if abs(cycles[cycle] - idy) <= 1 else "."
                crt_display[idx].append(value)
        return self._print_crt(crt_display)

    def _calculate_cycles(self) -> list[int]:
        cycles: list[int] = [1]
        for line in self.lines:
            cycles.extend(self._next_cycles(line, cycles))
        return cycles

    def _next_cycles(self, line: str, cycles: list[int]) -> list[int]:
        last_value = cycles[-1]
        if line == "noop":
            return [last_value]
        return [last_value, self._parse_line(line) + last_value]

    @staticmethod
    def _parse_line(line: str) -> int:
        regex = re.compile(r".* (?P<value>.*)")
        matches = regex.search(line)
        assert matches
        value = int(matches.group("value"))
        return value

    @staticmethod
    def _print_crt(crt_display: list[list[str]]) -> list[str]:
        return ["".join(line) for line in crt_display]
