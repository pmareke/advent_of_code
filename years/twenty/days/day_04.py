import re
from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class Day04:
    lines: list[str]

    def part_one(self) -> int:
        result = 0
        lines = "\n".join(self.lines)
        for line in lines.split("\n\n"):
            passport = " ".join(line.split("\n"))
            if self._is_valid(passport):
                result += 1
        return result

    def part_two(self) -> int:
        result = 0
        lines = "\n".join(self.lines)
        for line in lines.split("\n\n"):
            passport = " ".join(line.split("\n"))
            if self._is_valid_part_two(passport):
                result += 1
        return result

    @staticmethod
    def _is_valid(passport: str) -> bool:
        fields = passport.split(" ")
        present_fields = set(field.split(":")[0] for field in fields)
        if len(present_fields) == 8:
            return True
        if len(present_fields) == 7 and "cid" not in present_fields:
            return True
        return False

    def _is_valid_part_two(self, passport: str) -> bool:
        if not self._is_valid(passport):
            return False
        fields = passport.split(" ")
        valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        rules: dict[str, Callable] = {
            "byr": lambda year: 1920 <= int(year) <= 2002,
            "iyr": lambda year: 2010 <= int(year) <= 2020,
            "eyr": lambda year: 2020 <= int(year) <= 2030,
            "hgt": self._validate_height,
            "hcl": self._validate_color,
            "ecl": lambda color: color in valid_colors,
            "pid": lambda number: len(number) == 9,
            "cid": lambda _: True,
        }
        for field in fields:
            key, value = field.split(":")
            if not rules[key](value):
                return False
        return True

    @staticmethod
    def _validate_color(color: str) -> bool:
        return color.startswith("#") and bool(re.search(r"([a-z]|[0-9])", color))

    @staticmethod
    def _validate_height(height: str) -> bool:
        if height.endswith("cm"):
            return 150 <= int(height[:-2]) <= 193
        if height.endswith("in"):
            return 59 <= int(height[:-2]) <= 76
        return False
