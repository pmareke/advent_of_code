from expects import equal, expect

from years.twenty_two.days.day_13 import Day13


class TestDay13:
    def setup(self) -> None:
        with open("years/twenty_two/inputs/13.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day13(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(5366))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(23391))
