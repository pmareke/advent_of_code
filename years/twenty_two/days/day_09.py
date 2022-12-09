from dataclasses import dataclass

DX = {"L": 0, "U": -1, "R": 0, "D": 1}
DY = {"L": -1, "U": 0, "R": 1, "D": 0}


@dataclass
class Day09:
    lines: list[str]

    def part_one(self) -> int:
        head = (0, 0)
        tail = (0, 0)
        positions = set()
        for line in self.lines:
            direction, steps = line.split(" ")
            for _ in range(int(steps)):
                positions.add(tail)
                head = (head[0] + DX[direction], head[1] + DY[direction])
                tail = self._calculate_knot(head, tail)
                positions.add(tail)
        return len(positions)

    def part_two(self) -> int:
        head = (0, 0)
        tails = [(0, 0) for _ in range(9)]
        positions = set()
        for line in self.lines:
            direction, steps = line.split(" ")
            for _ in range(int(steps)):
                positions.add(tails[-1])
                head = (head[0] + DX[direction], head[1] + DY[direction])
                tails[0] = self._calculate_knot(head, tails[0])  # type: ignore
                for i in range(1, 9):
                    tails[i] = self._calculate_knot(tails[i - 1], tails[i])  # type: ignore
                positions.add(tails[-1])
        return len(positions)

    @staticmethod
    def _calculate_knot(
        head: tuple[int, int], tail: tuple[int, int]
    ) -> tuple[int, int]:
        x_distance = head[0] - tail[0]
        y_distance = head[1] - tail[1]
        if abs(x_distance) >= 2 and abs(y_distance) >= 2:
            x_tail = head[0] - 1 if tail[0] < head[0] else head[0] + 1
            y_tail = head[1] - 1 if tail[1] < head[1] else head[1] + 1
            return (x_tail, y_tail)
        if abs(x_distance) >= 2:
            x_tail = head[0] - 1 if tail[0] < head[0] else head[0] + 1
            return (x_tail, head[1])
        if abs(y_distance) >= 2:
            y_tail = head[1] - 1 if tail[1] < head[1] else head[1] + 1
            return (head[0], y_tail)
        return tail
