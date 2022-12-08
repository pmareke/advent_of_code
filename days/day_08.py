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
        forest = self._build_forest()
        return max(self._find_scenic_scores(forest))

    def _build_forest(self) -> list[list[int]]:
        forest: list[list[int]] = []
        for line in self.lines:
            forest.append([int(tree) for tree in line])
        return forest

    @staticmethod
    def _find_visible_trees(forest: list[list[int]]) -> int:
        visible = 0
        for index_x in range(1, len(forest) - 1):
            for index_y in range(1, len(forest[0]) - 1):
                tree = forest[index_x][index_y]
                top = bottom = left = right = True
                for index_i in range(0, index_x):
                    if tree <= forest[index_i][index_y]:
                        top = False
                for index_i in range(0, index_y):
                    if tree <= forest[index_x][index_i]:
                        left = False
                for index_i in range(index_y + 1, len(forest[0])):
                    if tree <= forest[index_x][index_i]:
                        right = False
                for index_i in range(index_x + 1, len(forest)):
                    if tree <= forest[index_i][index_y]:
                        bottom = False
                if any([top, bottom, left, right]):
                    visible += 1
        return visible

    @staticmethod
    def _find_scenic_scores(forest: list[list[int]]) -> list[int]:
        scenic_scores: list[int] = [0]
        for index_x in range(1, len(forest) - 1):
            for index_y in range(1, len(forest[0]) - 1):
                tree = forest[index_x][index_y]
                top_neighbours = (
                    bottom_neighbours
                ) = left_neighbours = right_neighbours = 0
                for index_i in range(0, index_x):
                    neighbour = forest[index_x - index_i - 1][index_y]
                    top_neighbours += 1
                    if tree <= neighbour:
                        break
                for index_i in range(index_x + 1, len(forest)):
                    neighbour = forest[index_i][index_y]
                    bottom_neighbours += 1
                    if tree <= neighbour:
                        break
                for index_i in range(0, index_y):
                    neighbour = forest[index_x][index_y - index_i - 1]
                    left_neighbours += 1
                    if tree <= neighbour:
                        break
                for index_i in range(index_y + 1, len(forest[0])):
                    neighbour = forest[index_x][index_i]
                    right_neighbours += 1
                    if tree <= neighbour:
                        break
                scenic_scores.append(
                    top_neighbours
                    * bottom_neighbours
                    * left_neighbours
                    * right_neighbours
                )
        return scenic_scores
