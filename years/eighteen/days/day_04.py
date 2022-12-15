import re
from dataclasses import dataclass


@dataclass
class Time:
    year: int
    month: int
    day: int
    hour: int
    minute: int


@dataclass
class Guard:
    guard_id: int
    slots_sleeps:list[Time] = []
    slots_awakes: list[Time] = []

    def sleep(self, time: Time) -> None:
        self.slots_sleeps.append(time)

    def awake(self, time: Time) -> None:
        self.slots_awakes.append(time)

@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        guards: dict[int, Guard] = {}         
        for line in self.lines:
            entry = self._parse(line)
            guard = self._create_guard_from(entry)
            guards[guard.guard_id]= guard
        return 0

    def part_two(self) -> int:
        return 0

    @staticmethod
    def _parse(line: str) -> tuple:
        regex = re.compile(
            r"\[ (?P<year>\d+)-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] (?P<guard>Guard #(\d+) (.*)|(.*))"
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

    @staticmethod
    def _create_guard_from(entry: tuple) -> Guard:
        pass
