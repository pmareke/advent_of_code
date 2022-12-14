from dataclasses import dataclass


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        result = 0
        for line in self.lines:
            words = line.split(" ")
            if len(words) == len(set(words)):
                result += 1
        return result

    def part_two(self) -> int:
        result = 0
        for line in self.lines:
            words = line.split(" ")
            if not self._is_anagram(words):
                result += 1
        return result

    @staticmethod
    def _is_anagram(words: list[str]) -> bool:
        for idx in range(len(words)):
            for idy in range(1, len(words)):
                if idx == idy:
                    continue
                if sorted(words[idx]) == sorted(words[idy]):
                    return True
        return False
