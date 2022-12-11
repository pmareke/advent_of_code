from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        two_times = three_times = 0
        for line in self.lines:
            occurrences: dict[str, int] = defaultdict(int)
            for letter in line:
                occurrences[letter] += 1
            if any([True for occurrence in occurrences.values() if occurrence == 2]):
                two_times += 1
            if any([True for occurrence in occurrences.values() if occurrence == 3]):
                three_times += 1
        return two_times * three_times

    def part_two(self) -> str:
        common_letters = ""
        for index, line in enumerate(self.lines):
            for i in range(index + 1, len(self.lines)):
                diff = []
                for idx, letter in enumerate(line):
                    if letter != self.lines[i][idx]:
                        diff.append(letter)
                if len(diff) == 1:
                    diff_index = line.index(diff[0])
                    return line[0:diff_index] + line[diff_index + 1 :]
        return common_letters
