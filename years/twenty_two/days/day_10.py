import re
from dataclasses import dataclass


@dataclass
class Day10:
    lines: list[str]

    def part_one(self) -> int:
        cycles = self._calculate_cycles()
        return sum((idx + 1) * cycles[idx] for idx in range(19, 220, 40))

    def part_two(self) -> None:
        cycles = self._calculate_cycles()
        crt_display: list[list[str]] = []
        for idx in range(6):
            crt_display.append([])
            for idy in range(40):
                cycle = (idx * 40) + idy
                value = "#" if abs(cycles[cycle] - idy) <= 1 else "."
                crt_display[idx].append(value)
        self._print_crt(crt_display)

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
    def _print_crt(crt_display: list[list[str]]) -> None:
        print(["".join(line) for line in crt_display])
