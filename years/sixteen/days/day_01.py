from dataclasses import dataclass


@dataclass
class Day01:
    lines: list[str]

    def part_one(self) -> int:
        DX: list[int] = [0, 1, 0, -1]
        DY: list[int] = [-1, 0, 1, 0]
        d = x = y = 0
        for line in self.lines[0].split(", "):
            z = 3 if line[0] == "L" else 1
            d = (d + z) % 4
            distance = int(line[1:])
            x += DX[d] * distance
            y += DY[d] * distance
        return abs(x) + abs(y)

    def part_two(self) -> int:
        seen: set[str] = set()
        DX: list[int] = [0, 1, 0, -1]
        DY: list[int] = [-1, 0, 1, 0]
        d = x = y = 0
        try:
            for line in self.lines[0].split(", "):
                z = 3 if line[0] == "L" else 1
                d = (d + z) % 4
                distance = int(line[1:])
                for _ in range(0, distance):
                    x += DX[d]
                    y += DY[d]
                    pair = f"{x}:{y}"
                    if pair in seen:
                        raise Exception
                    seen.add(pair)
            return 0
        except Exception:
            return abs(x) + abs(y)
