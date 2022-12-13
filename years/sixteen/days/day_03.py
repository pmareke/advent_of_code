from dataclasses import dataclass


@dataclass
class Day03:
    lines: list[str]

    def part_one(self) -> int:
        valid = 0
        for line in self.lines:
            triangle = list(map(int, line.split()))
            print(triangle)
            if self._is_valid(triangle):
                valid += 1
        return valid

    def part_two(self) -> int:
        valid = 0
        triangles: list[list[int]] = []
        for line in self.lines:
            triangles.append(list(map(int, line.split())))
        for index in range(0, len(triangles), 3):
            for idx in [0, 1, 2]:
                x = triangles[index][idx]
                y = triangles[index + 1][idx]
                z = triangles[index + 2][idx]
                if self._is_valid([x, y, z]):
                    valid += 1
        return valid

    @staticmethod
    def _is_valid(triangle: list[int]) -> bool:
        x, y, z = triangle
        return x + y > z and x + z > y and y + z > x
