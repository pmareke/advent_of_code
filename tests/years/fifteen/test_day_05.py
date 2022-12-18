from expects import equal, expect

from years.fifteen.days.day_05 import Day05


class TestDay05:
    def setup(self) -> None:
        with open("years/fifteen/inputs/5.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day05(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(238))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(69))
