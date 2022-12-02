import re


class Day02:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines

    def part_one(self) -> int:
        score = 0
        for line in self.lines:
            player_a, player_b = self._read_moves(line)
            score += self._play_round(player_a, player_b)
        return score

    def _play_round(self, player_a: str, player_b: str) -> int:
        b_points = {"X": 1, "Y": 2, "Z": 3}[player_b]
        scores = {
            "A": {"X": 3, "Y": 6, "Z": 0},
            "B": {"X": 0, "Y": 3, "Z": 6},
            "C": {"X": 6, "Y": 0, "Z": 3},
        }
        return scores[player_a][player_b] + b_points

    def part_two(self) -> int:
        score = 0
        for line in self.lines:
            player_a, result = self._read_moves(line)
            score += self._play_round_with_winner(player_a, result)
        return score

    def _play_round_with_winner(self, player_a: str, result: str) -> int:
        a_points = {"A": 1, "B": 2, "C": 3}
        scores = {
            "Y": {
                "A": 3 + a_points[player_a],
                "B": 3 + a_points[player_a],
                "C": 3 + a_points[player_a],
            },
            "Z": {
                "A": 6 + a_points["B"],
                "B": 6 + a_points["C"],
                "C": 6 + a_points["A"],
            },
            "X": {
                "A": 0 + a_points["C"],
                "B": 0 + a_points["A"],
                "C": 0 + a_points["B"],
            },
        }
        return scores[result][player_a]

    @staticmethod
    def _read_moves(line: str) -> tuple[str, str]:
        move_regex = re.compile(r"(?P<A>[ABC]) (?P<B>[XYZ])")
        matches = move_regex.search(line)
        if not matches:
            raise Exception
        player_a = matches.group("A")
        player_b = matches.group("B")
        return (player_a, player_b)
