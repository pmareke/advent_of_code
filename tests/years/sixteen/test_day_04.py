from expects import equal, expect

from years.sixteen.days.day_04 import Day04


class TestDay04:
    def setup(self) -> None:
        with open("years/sixteen/inputs/4.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day04(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(361724))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(482))
