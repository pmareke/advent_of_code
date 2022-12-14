from expects import equal, expect

from years.twenty_two.days.day_07 import Day07


class TestDay07:
    def setup(self) -> None:
        with open("years/twenty_two/inputs/7.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day07(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(1297683))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(5756764))
