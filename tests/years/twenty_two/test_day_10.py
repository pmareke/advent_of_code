from expects import equal, expect

from years.twenty_two.days.day_10 import Day10


class TestDay01:
    def setup(self) -> None:
        with open("years/twenty_two/inputs/10.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day10(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(13220))
