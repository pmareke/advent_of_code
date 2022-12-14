from expects import equal, expect

from years.twenty_two.days.day_14 import Day14


class TestDay14:
    def setup(self) -> None:
        with open("years/twenty_two/inputs/14.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day14(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(592))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(30367))
