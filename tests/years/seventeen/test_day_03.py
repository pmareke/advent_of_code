from expects import equal, expect

from years.seventeen.days.day_03 import Day03


class TestDay03:
    def setup(self) -> None:
        with open("years/seventeen/inputs/3.in") as file:
            number = int(file.readlines()[0])
            self.day = Day03(number)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(430))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(312453))
