import pytest
from expects import equal, expect

from days.day_02 import Day02


class TestDay02:
    @pytest.fixture
    def lines(self) -> list[str]:
        return [line.strip() for line in open("inputs/2.in")]

    def test_part_one(self, lines: list[str]) -> None:
        day = Day02(lines)

        result = day.part_one()

        expect(result).to(equal(0))

    def test_part_two(self, lines: list[str]) -> None:
        day = Day02(lines)

        result = day.part_two()

        expect(result).to(equal(0))
