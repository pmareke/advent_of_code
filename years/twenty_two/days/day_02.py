import re
from dataclasses import dataclass


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        score = 0
        for line in self.lines:
            oponent, myself = self._parse_hand(line)
            score += self._play_round(oponent, myself)
        return score

    def part_two(self) -> int:
        score = 0
        for line in self.lines:
            oponent, myself = self._parse_hand(line)
            score += self._play_round_with_winner(oponent, myself)
        return score

    def _play_round(self, oponent: str, myself: str) -> int:
        points_map = {
            "A": {"X": 3, "Y": 6, "Z": 0},
            "B": {"X": 0, "Y": 3, "Z": 6},
            "C": {"X": 6, "Y": 0, "Z": 3},
        }
        hand_score = points_map[oponent][myself]
        extra_points = {"X": 1, "Y": 2, "Z": 3}
        return hand_score + extra_points[myself]

    def _play_round_with_winner(self, oponent: str, myself: str) -> int:
        points_map = {
            "Y": {"A": 1, "B": 2, "C": 3},
            "Z": {"A": 2, "B": 3, "C": 1},
            "X": {"A": 3, "B": 1, "C": 2},
        }
        hand_score = points_map[myself][oponent]
        extra_points = {"X": 0, "Y": 3, "Z": 6}
        return hand_score + extra_points[myself]

    @staticmethod
    def _parse_hand(line: str) -> tuple[str, str]:
        move_regex = re.compile(r"(?P<oponent>[ABC]) (?P<myself>[XYZ])")
        matches = move_regex.search(line)
        assert matches
        oponent = matches.group("oponent")
        myself = matches.group("myself")
        return (oponent, myself)
