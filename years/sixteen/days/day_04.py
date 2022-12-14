from collections import defaultdict
from dataclasses import dataclass
import re


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        result = 0
        for line in self.lines:
            ocurrences, sector_id, checksum = self._parse(line)
            keys = "".join(ocurrences.keys())
            if keys.startswith(checksum):
                result += sector_id
        return result

    def part_two(self) -> int:
        for line in self.lines:
            room, sector = line.rsplit("-", 1)
            sector_id = int(sector.split("[")[0])
            word = ""
            for letter in room:
                times = sector_id % 26
                new_letter = ord(letter) - ord("a") + times
                word += chr((new_letter % 26) + ord("a"))
            if "north" in word:
                return sector_id
        return 0

    @staticmethod
    def _parse(line: str) -> tuple:
        regex = re.compile(r"(?P<name>[a-z]+)(?P<id>\d+)\[(?P<checksum>\w+)\]")
        matches = regex.search(line.replace("-", ""))
        assert matches
        letters = matches.group("name")
        ocurrences: dict[str, int] = defaultdict(int)
        for letter in letters:
            ocurrences[letter] += 1
        sort_ocurrences = sorted(ocurrences.items(), key=lambda x: (-x[1], x[0]))
        sector_id = int(matches.group("id"))
        checksum = matches.group("checksum")
        return (dict(sort_ocurrences), sector_id, checksum)
