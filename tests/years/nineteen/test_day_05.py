from expects import equal, expect

from years.nineteen.days.day_05 import Day05


class TestDay05:
    def setup(self) -> None:
        with open("years/nineteen/inputs/5.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day05(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(5821753))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(11956381))
