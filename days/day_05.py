import re
from dataclasses import dataclass


@dataclass
class Instruction:
    items: int
    origin: int
    destination: int


@dataclass
class Day05:
    file: str

    def part_one(self) -> str:
        stacks, instructions = self._parse_file()
        for instruction in instructions:
            items = stacks[instruction.origin - 1][: instruction.items]
            for item in items:
                stacks[instruction.origin - 1].pop(0)
                stacks[instruction.destination - 1].insert(0, item)
        return "".join([stack[0] for stack in stacks])

    def part_two(self) -> str:
        stacks, instructions = self._parse_file()
        for instruction in instructions:
            items = []
            for _ in range(instruction.items):
                items.append(stacks[instruction.origin - 1].pop(0))
            for item in reversed(items):
                stacks[instruction.destination - 1].insert(0, item)
        return "".join([stack[0] for stack in stacks])

    def _parse_file(self) -> tuple[list[list[str]], list[Instruction]]:
        top, bottom = self.file.split("\n\n")
        stacks = self._parse_top(top)
        instructions = self._parse_bottom(bottom)
        return stacks, instructions

    def _parse_top(self, top: str) -> list[list[str]]:
        stacks: list[list[str]] = []
        for line in top.split("\n")[:-1]:
            items = self._parse_stacks_line(line)
            for index, letter in enumerate(items):
                if index >= len(stacks):
                    stacks.append([])
                if not letter == " ":
                    stacks[index].append(letter)
        return stacks

    @staticmethod
    def _parse_stacks_line(line: str) -> list[str]:
        return [line[index] for index in range(1, len(line), 4)]

    def _parse_bottom(self, bottom: str) -> list[Instruction]:
        instructions: list[Instruction] = []
        for line in bottom.strip().split("\n"):
            instructions.append(self._parse_instruction(line))
        return instructions

    @staticmethod
    def _parse_instruction(line: str) -> Instruction:
        regex = re.compile(
            r"move (?P<items>\d+) from (?P<origin>\d+) to (?P<destination>\d+)"
        )
        matches = regex.search(line)
        assert matches
        items = int(matches.group("items"))
        origin = int(matches.group("origin"))
        destination = int(matches.group("destination"))
        return Instruction(items, origin, destination)
