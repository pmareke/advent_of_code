from dataclasses import dataclass


@dataclass
class Day08:
    lines: list[str]

    def part_one(self) -> int:
        forest = self._build_forest()
        top_line = bottom_line = len(forest[0])
        left_line = right_line = len(forest) - 2
        visible_from_the_egde = top_line + bottom_line + left_line + right_line
        visible_from_the_inside = self._find_visible_trees(forest)
        return visible_from_the_egde + visible_from_the_inside

    def part_two(self) -> int:
        score = 0
        return score

    def _build_forest(self) -> list[list[int]]:
        forest: list[list[int]] = []
        for line in self.lines:
            forest.append([int(tree) for tree in line])
        return forest

    @staticmethod
    def _find_visible_trees(forest: list[list[int]]) -> int:
        visible = 0
        for x in range(1, len(forest) - 1):
            for y in range(1, len(forest[0]) - 1):
                tree = forest[x][y]
                print(tree)
        return visible
