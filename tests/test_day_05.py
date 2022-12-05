from expects import equal, expect

from days.day_05 import Day05


class TestDay05:
    def setup(self) -> None:
        with open("inputs/5.in") as file:
            self.day = Day05(file.read())

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal("JRVNHHCSJ"))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal("GNFBSBJLH"))
