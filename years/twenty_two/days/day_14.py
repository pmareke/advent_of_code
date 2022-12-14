from dataclasses import dataclass


@dataclass
class Day14:
    lines: list[str]

    def part_one(self) -> int:
        return self._solve()

    def part_two(self) -> int:
        return self._solve(part_two=True)

    def _solve(self, part_two: bool = False) -> int:
        packets = self._parse()

        floor = 2 + max(packet[1] for packet in packets)
        low_x = min(packet[0] for packet in packets) - 2000
        hi_x = max(packet[0] for packet in packets) + 2000
        for value in range(low_x, hi_x):
            packets.add((value, floor))

        times = 0
        origin = (500, 0)
        while True:
            rock = origin
            while True:
                if rock[1] + 1 >= floor and not part_two:
                    return times
                if (rock[0], rock[1] + 1) not in packets:
                    rock = (rock[0], rock[1] + 1)
                elif (rock[0] - 1, rock[1] + 1) not in packets:
                    rock = (rock[0] - 1, rock[1] + 1)
                elif (rock[0] + 1, rock[1] + 1) not in packets:
                    rock = (rock[0] + 1, rock[1] + 1)
                else:
                    break
            times += 1
            if rock == origin:
                return times
            packets.add(rock)

    def _parse(self) -> set:
        packets: set[tuple[int, int]] = set()
        for line in self.lines:
            previous: list[int] = []
            for point in line.split("->"):
                x_point, y_point = map(int, point.split(","))
                if previous:
                    diff_x = x_point - previous[0]  # type: ignore
                    diff_y = y_point - previous[1]
                    difference = max(abs(diff_x), abs(diff_y))
                    for idiff_x in range(difference + 1):
                        new_x = previous[0] + idiff_x * (
                            1 if diff_x > 0 else (-1 if diff_x < 0 else 0)
                        )
                        new_y = previous[1] + idiff_x * (
                            1 if diff_y > 0 else (-1 if diff_y < 0 else 0)
                        )
                        packets.add((new_x, new_y))
                previous = [x_point, y_point]
        return packets
