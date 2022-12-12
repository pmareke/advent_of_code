from expects import equal, expect

from years.twenty_two.days.day_12 import Day12


class TestDay12:
    def setup(self) -> None:
        with open("years/twenty_two/inputs/12.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day12(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(352))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(345))
