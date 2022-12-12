from expects import equal, expect

from years.nineteen.days.day_03 import Day03


class TestDay03:
    def setup(self) -> None:
        with open("years/nineteen/inputs/3.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day03(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(4981))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(164012))
