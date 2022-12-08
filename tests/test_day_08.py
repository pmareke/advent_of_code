from expects import equal, expect

from days.day_08 import Day08


class TestDay08:
    def setup(self) -> None:
        with open("inputs/8.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day08(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(1851))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(574080))
