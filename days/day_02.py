import re
from dataclasses import dataclass


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        score = 0
        for line in self.lines:
            oponent, myself = self._read_moves(line)
            score += self._play_round(oponent, myself)
        return score

    def _play_round(self, oponent: str, myself: str) -> int:
        points = {"X": 1, "Y": 2, "Z": 3}[myself]
        scores = {
            "A": {"X": 3, "Y": 6, "Z": 0},
            "B": {"X": 0, "Y": 3, "Z": 6},
            "C": {"X": 6, "Y": 0, "Z": 3},
        }
        return scores[oponent][myself] + points

    def part_two(self) -> int:
        score = 0
        for line in self.lines:
            oponent, result = self._read_moves(line)
            score += self._play_round_with_winner(oponent, result)
        return score

    def _play_round_with_winner(self, oponent: str, result: str) -> int:
        points = {"A": 1, "B": 2, "C": 3}
        scores = {
            "Y": {
                "A": 3 + points[oponent],
                "B": 3 + points[oponent],
                "C": 3 + points[oponent],
            },
            "Z": {
                "A": 6 + points["B"],
                "B": 6 + points["C"],
                "C": 6 + points["A"],
            },
            "X": {
                "A": 0 + points["C"],
                "B": 0 + points["A"],
                "C": 0 + points["B"],
            },
        }
        return scores[result][oponent]

    @staticmethod
    def _read_moves(line: str) -> tuple[str, str]:
        move_regex = re.compile(r"(?P<A>[ABC]) (?P<B>[XYZ])")
        matches = move_regex.search(line)
        if not matches:
            raise Exception
        oponent = matches.group("A")
        myself = matches.group("B")
        return (oponent, myself)
