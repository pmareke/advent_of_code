import pytest
from expects import equal, expect

from days.day_06 import Day06


def read_input() -> str:
    with open("inputs/6.in") as file:
        return file.readline().strip()


class TestDay06:
    @pytest.mark.parametrize(
        "signal,expected_result",
        [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
            (read_input(), 1848),
        ],
    )
    def test_part_one(self, signal: str, expected_result: int) -> None:
        day = Day06(signal)
        result = day.part_one()

        expect(result).to(equal(expected_result))

    @pytest.mark.parametrize(
        "signal,expected_result",
        [
            ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
            ("nppdvjthqldpwncqszvftbrmjlhg", 23),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
            (read_input(), 2308),
        ],
    )
    def test_part_two(self, signal: str, expected_result: int) -> None:
        day = Day06(signal)
        result = day.part_two()

        expect(result).to(equal(expected_result))
