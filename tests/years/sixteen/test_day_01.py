from expects import equal, expect

from years.sixteen.days.day_01 import Day01


class TestDay01:
    def setup(self) -> None:
        with open("years/sixteen/inputs/1.in") as file:
            lines = [line.strip() for line in file]
            self.day = Day01(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(271))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(153))
