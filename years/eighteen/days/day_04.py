from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Counter


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        guards = self._solve()
        total_time_by_guard: list[tuple[int, int]] = []
        for guard_id, times in guards.items():
            total_time: int = sum(times.values())
            total_time_by_guard.append((total_time, guard_id))
        _, guard_id = max(total_time_by_guard)
        return int(guard_id * guards[guard_id].most_common()[0][0])

    def part_two(self) -> int:
        guards = self._solve()
        most_common_minute_by_guard: list[tuple[tuple, int]] = []
        for guard_id, times in guards.items():
            most_common: tuple[int, int] = times.most_common()[0][::-1]
            most_common_minute_by_guard.append((most_common, guard_id))
        (_, minute), guard_id = max(most_common_minute_by_guard)
        return int(guard_id * minute)

    def _solve(self) -> dict[int, Counter]:
        guards: dict[int, Counter] = defaultdict(Counter)
        start: datetime = datetime.now()
        guard: int = 0
        for line in sorted(self.lines):
            str_time, instruction = line.split("] ")
            time = datetime.strptime(str_time, "[%Y-%m-%d %H:%M")
            if "#" in instruction:
                guard = int(instruction.split("#")[1].split()[0])
            if "falls" in instruction:
                start = time
            if "wakes" in instruction:
                diff_minutes = int((time - start).total_seconds() // 60)
                times_by_minute = Counter(
                    (start.minute + i) % 60 for i in range(diff_minutes)
                )
                guards[guard].update(times_by_minute)
        return guards
