import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


class Bingo:
    def __init__(
        self, bingo_id: int, columns: list[list[int]], rows: list[list[int]]
    ) -> None:
        self.bingo_id = bingo_id
        self.columns = columns
        self.rows = rows

    def play(self, played_number: int) -> bool:
        for idx, column in enumerate(self.columns):
            for idy, number in enumerate(column):
                if number == played_number:
                    self.columns[idx].pop(idy)
                    if not self.columns[idx]:
                        return True
        for idx, row in enumerate(self.rows):
            for idy, number in enumerate(row):
                if number == played_number:
                    self.rows[idx].pop(idy)
                    if not self.rows[idx]:
                        return True
        return False

    @property
    def score(self) -> int:
        return sum([sum(numbers) for numbers in self.columns])


@dataclass
class Game:
    bingos: dict[int, Bingo]

    def play(self, number: int) -> Optional[Bingo]:
        for bingo in self.bingos.values():
            if bingo.play(number):
                return bingo
        return None


class BingoBuilder:
    @staticmethod
    def from_group(bingo_id: int, group: str) -> Bingo:
        columns: list[list[int]] = []
        rows: list[list[int]] = []
        for line in group.split("\n"):
            numbers = list(map(int, re.findall(r"(\d+)", line)))
            columns.append(numbers)
        for idx in range(len(columns[0])):
            rows.append([])
            for column in columns:
                rows[idx].append(column[idx])
        return Bingo(bingo_id, columns, rows)


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        numbers = list(map(int, self.lines[0].split(",")))
        bingos = self._generate_bingo(self.lines[2:])
        game = Game(bingos)
        for number in numbers:
            winner = game.play(number)
            if winner:
                return winner.score * number
        return 0

    def part_two(self) -> int:
        numbers = list(map(int, self.lines[0].split(",")))
        bingos = self._generate_bingo(self.lines[2:])
        winners: list[int] = []
        while True:
            left_bingos = bingos.copy()
            for winner in winners:
                del left_bingos[winner]
            game = Game(left_bingos)
            for number in numbers:
                bingo_winner = game.play(number)
                if bingo_winner:
                    winners.append(bingo_winner.bingo_id)
                    if len(winners) == len(bingos):
                        return bingo_winner.score * number
                    break

    @staticmethod
    def _generate_bingo(lines: list[str]) -> dict[int, Bingo]:
        bingos: dict[int, Bingo] = defaultdict()
        for idx, group in enumerate("\n".join(lines).split("\n\n")):
            bingos[idx] = BingoBuilder.from_group(idx, group)
        return bingos
