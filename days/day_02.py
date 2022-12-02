import re


class Day02:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines

    def part_one(self) -> int:
        move_regex = re.compile(r"(?P<A>[ABC]) (?P<B>[XYZ])")
        score = 0
        for line in self.lines:
            matches = move_regex.search(line)
            if not matches:
                raise Exception
            player_a = matches.group("A")
            player_b = matches.group("B")
            score += self._play_round(player_a, player_b)
        return score

    def _play_round(self, player_a: str, player_b: str) -> int:
        b_points = {"X": 1, "Y": 2, "Z": 3}[player_b]
        scores = {
            "A": {
                "X": 3 + b_points,
                "Y": 6 + b_points,
                "Z": 0 + b_points,
            },
            "B": {
                "Y": 3 + b_points,
                "Z": 6 + b_points,
                "X": 0 + b_points,
            },
            "C": {
                "Z": 3 + b_points,
                "X": 6 + b_points,
                "Y": 0 + b_points,
            },
        }
        return scores[player_a][player_b]

    def part_two(self) -> int:
        move_regex = re.compile(r"(?P<A>[ABC]) (?P<B>[XYZ])")
        score = 0
        for line in self.lines:
            matches = move_regex.search(line)
            if not matches:
                raise Exception
            player_a = matches.group("A")
            result = matches.group("B")
            score += self._play_round_with_winner(player_a, result)
        return score

    def _play_round_with_winner(self, player_a: str, result: str) -> int:
        a_points = {"A": 1, "B": 2, "C": 3}
        if result == "Y":
            return 3 + a_points[player_a]
        scores = {
            "Z": {
                "B": 6 + a_points["C"],
                "A": 6 + a_points["B"],
                "C": 6 + a_points["A"],
            },
            "X": {
                "B": 0 + a_points["A"],
                "A": 0 + a_points["C"],
                "C": 0 + a_points["B"],
            },
        }
        return scores[result][player_a]
