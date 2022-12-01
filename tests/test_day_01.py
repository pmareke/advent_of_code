from expects import equal, expect

from days.day_01 import Day01


class TestDay01:
    def setup(self, lines: list[str]) -> None: 
        lines = [line.strip() for line in open("inputs/1.in")]
        self.day = Day01(lines)

    def test_part_one(self) -> None:
        result = self.day.part_one()

        expect(result).to(equal(72070))

    def test_part_two(self) -> None:
        result = self.day.part_two()

        expect(result).to(equal(211805))
