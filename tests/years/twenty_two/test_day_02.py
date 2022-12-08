from expects import equal, expect

from years.twenty_two.days.day_02 import Day02


class TestDay02:
    def setup(self) -> None:
        with open("years/twenty_two/inputs/2.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day02(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(13005))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(11373))
