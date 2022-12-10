import re
from dataclasses import dataclass


@dataclass
class Day10:
    lines: list[str]

    def part_one(self) -> int:
        cycles = self._calculate_cycles()
        first_cycle, last_cycle, step = [19, 220, 40]
        return sum(
            (idx + 1) * cycles[idx] for idx in range(first_cycle, last_cycle, step)
        )

    def part_two(self) -> list[str]:
        crt_high = 6
        crt_wide = 40
        cycles = self._calculate_cycles()
        crt_display: list[list[str]] = []
        for idx in range(crt_high):
            crt_display.append([])
            for idy in range(crt_wide):
                cycle = (idx * crt_wide) + idy
                value = "#" if abs(cycles[cycle] - idy) <= 1 else "."
                crt_display[idx].append(value)
        return self._print_crt(crt_display)

    def _calculate_cycles(self) -> list[int]:
        cycles: list[int] = [1]
        for line in self.lines:
            last_value = cycles[-1]
            if line == "noop":
                cycles.append(last_value)
                continue
            value = self._parse_line(line)
            cycles.extend([last_value, last_value + value])
        return cycles

    @staticmethod
    def _parse_line(line: str) -> int:
        regex = re.compile(r"(?P<operation>.*) (?P<value>.*)")
        matches = regex.search(line)
        assert matches
        value = int(matches.group("value"))
        return value

    @staticmethod
    def _print_crt(crt_display: list[list[str]]) -> list[str]:
        return ["".join(line) for line in crt_display]
