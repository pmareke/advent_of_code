from dataclasses import dataclass


@dataclass
class Day02:
    lines: list[str]

    def part_one(self) -> int:
        return self._solve(noun=12, verb=2)

    def part_two(self) -> int:
        noun = verb = 0
        for x in range(100):
            for y in range(100):
                result = self._solve(x, y)
                if result == 19690720:
                    noun = x
                    verb = y
                    break
        return (noun * 100) + verb

    def _solve(self, noun: int, verb: int) -> int:
        line = self.lines[0]
        code = list(map(int, line.split(",")))
        code[1] = noun
        code[2] = verb
        i = 0
        while True:
            op, op1, op2, pointer = code[i : i + 4]
            if op == 99:
                i += 1
                break
            if op == 1:
                i += 4
                code[pointer] = code[op1] + code[op2]
            if op == 2:
                i += 4
                code[pointer] = code[op1] * code[op2]
        return code[0]
