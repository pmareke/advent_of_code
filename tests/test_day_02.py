import pytest
from expects import equal, expect

from days.day_02 import Day02


class TestDay02:
    def setup(self) -> None:
        lines = [line.strip() for line in open("inputs/2.in")]
        self.day = Day02(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(0))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(0))
