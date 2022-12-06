from expects import equal, expect

from days.day_07 import Day07


class TestDay07:
    def setup(self) -> None:
        with open("inputs/7.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day07(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(0))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(0))
