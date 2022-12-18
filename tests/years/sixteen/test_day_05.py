import pytest
from expects import equal, expect

from years.sixteen.days.day_05 import Day05


@pytest.mark.only_ci
class TestDay05:
    def setup(self) -> None:
        with open("years/sixteen/inputs/5.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day05(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal("4543c154"))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal("1050cbbd"))
