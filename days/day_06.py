from dataclasses import dataclass


@dataclass
class Day06:
    line: str

    def part_one(self) -> int:
        return self._find_start_of_packet()

    def part_two(self) -> int:
        return self._find_start_of_packet(part_two=True)

    def _find_start_of_packet(self, part_two: bool = False) -> int:
        number_of_characters = 14 if part_two else 4
        for index, _ in enumerate(self.line):
            if index + number_of_characters <= len(self.line):
                block = self.line[index : index + number_of_characters]
                if len(set(block)) == number_of_characters:
                    return index + number_of_characters
        return 0
