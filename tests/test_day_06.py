from expects import equal, expect

from days.day_06 import Day06


class TestDay06:
    def setup(self) -> None:
        with open("inputs/6.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day06(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(0))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(0))