from expects import equal, expect

from years.twenty_two.days.day_11 import Day11


class TestDay11:
    def setup(self) -> None:
        with open("years/twenty_two/inputs/11.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day11(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(58056))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(15048718170))
