from dataclasses import dataclass
from functools import cmp_to_key
from typing import Union


@dataclass
class Day13:
    lines: list[str]

    def part_one(self) -> int:
        lines = "\n".join(self.lines)
        packets = [line.split("\n") for line in lines.split("\n\n")]
        valid = 0
        for index, packet in enumerate(packets):
            left = eval(packet[0])
            right = eval(packet[1])
            if self._is_valid(left, right) == -1:
                valid += index + 1
        return valid

    def part_two(self) -> int:
        lines = "\n".join(self.lines)
        packets = []
        for line in lines.split("\n\n"):
            left, right = line.split("\n")
            packets.append(eval(left))
            packets.append(eval(right))
        packets.extend([[[2]], [[6]]])
        sorted_packets = sorted(packets, key=cmp_to_key(self._is_valid))
        result = 1
        for index, packet in enumerate(sorted_packets):
            if packet in [[[2]], [[6]]]:
                result *= index + 1
        return result

    def _is_valid(self, left: Union[list, int], right: Union[list, int]) -> int:
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                return 0
            return -1 if left < right else 1
        if isinstance(left, int) and isinstance(right, list):
            return self._is_valid([left], right)
        if isinstance(left, list) and isinstance(right, int):
            return self._is_valid(left, [right])
        if isinstance(left, list) and isinstance(right, list):
            i = 0
            while i < len(left) and i < len(right):
                is_valid = self._is_valid(left[i], right[i])
                if is_valid != 0:
                    return is_valid
                i += 1
            if i == len(left) and i < len(right):
                return -1
            if i == len(right) and i < len(left):
                return 1
            return 0
        return 0
