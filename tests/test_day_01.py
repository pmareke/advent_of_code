import pytest
from expects import equal, expect
from typing import List

from days.day_01 import Day01


class TestDay01:

    @pytest.fixture
    def lines(self) -> List[str]:
        return [line for line in open("inputs/1.in")]

    def test_part_one(self, lines: List[str]) -> None:
        day = Day01(lines)

        result = day.part_one()

        expect(result).to(equal(72070))

    def test_part_two(self, lines: List[str]) -> None:
        day = Day01(lines)

        result = day.part_two()

        expect(result).to(equal(211805))
