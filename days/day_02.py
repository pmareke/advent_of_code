import re


class Day02:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.move_map: dict[str, str] = {
            "A": "Rock",
            "X": "Rock",
            "B": "Paper",
            "Y": "Paper",
            "C": "Scissors",
            "Z": "Scissors",
        }
        self.move_score: dict[str, int] = {
            "Rock": 1,
            "Paper": 2,
            "Scissors": 3,
        }

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
        move_a = self.move_map[player_a]
        move_b = self.move_map[player_b]
        b_points = self.move_score[move_b]
        if move_a == move_b:
            return 3 + b_points
        if self.move_map[player_a] == "Rock":
            if self.move_map[player_b] == "Paper":
                return 6 + b_points
            if self.move_map[player_b] == "Scissors":
                return 0 + b_points
        if self.move_map[player_a] == "Paper":
            if self.move_map[player_b] == "Scissors":
                return 6 + b_points
            if self.move_map[player_b] == "Rock":
                return 0 + b_points
        if self.move_map[player_a] == "Scissors":
            if self.move_map[player_b] == "Rock":
                return 6 + b_points
            if self.move_map[player_b] == "Paper":
                return 0 + b_points
        return 0

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
        result_map: dict[str, str] = {
            "X": "Lose",
            "Y": "Draw",
            "Z": "Win",
        }
        move_a = self.move_map[player_a]
        expected_result = result_map[result]
        if expected_result == "Draw":
            return 3 + self.move_score[move_a]
        if expected_result == "Win":
            if move_a == "Paper":
                return 6 + self.move_score["Scissors"]
            if move_a == "Rock":
                return 6 + self.move_score["Paper"]
            if move_a == "Scissors":
                return 6 + self.move_score["Rock"]
        if expected_result == "Lose":
            if move_a == "Paper":
                return 0 + self.move_score["Rock"]
            if move_a == "Rock":
                return 0 + self.move_score["Scissors"]
            if move_a == "Scissors":
                return 0 + self.move_score["Paper"]
        return 0
