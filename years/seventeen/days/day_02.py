from dataclasses import dataclass


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        result = 0
        for line in self.lines:
            numbers = [int(number) for number in line.split("\t")]
            sort = sorted(numbers)
            result += sort[-1] - sort[0]
        return result

    def part_two(self) -> int:
        result = 0
        for line in self.lines:
            numbers = [int(number) for number in line.split("\t")]
            sort = sorted(numbers, reverse=True)
            for index, number in enumerate(sort):
                for i in range(index, len(sort)):
                    if i == len(sort) - 1:
                        break
                    if number % sort[i + 1] == 0:
                        result += number // sort[i + 1]
                        break
        return result
