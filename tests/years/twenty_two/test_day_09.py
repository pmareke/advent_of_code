from expects import equal, expect

from years.twenty_two.days.day_09 import Day09


class TestDay08:
    def setup(self) -> None:
        with open("years/twenty_two/inputs/9.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day09(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(6087))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(2493))
