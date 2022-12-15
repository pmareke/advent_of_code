import re
from dataclasses import dataclass


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        for line in self.lines:
            entry = self._parse(line)
            print(entry)
        return 0

    def part_two(self) -> int:
        return 0

    @staticmethod
    def _parse(line: str) -> tuple:
        regex = re.compile(
            r"\[(?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] (?P<guard>Guard #(\d+) (.*)|(.*))"
        )
        matches = regex.search(line)
        assert matches
        year = int(matches.group("year"))
        month = int(matches.group("month"))
        day = int(matches.group("day"))
        hour = int(matches.group("hour"))
        minute = int(matches.group("minute"))
        guard = matches.group("guard")
        return (year, month, day, hour, minute, guard)
