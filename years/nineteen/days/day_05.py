from dataclasses import dataclass


@dataclass
class Day05:
    lines: list[str]

    def part_one(self) -> int:
        return self._solve(input_id=1)

    def part_two(self) -> int:
        return self._solve(input_id=5)

    def _solve(self, input_id: int) -> int:
        line = self.lines[0]
        i = 0
        result = 0
        code = list(map(int, line.split(",")))
        while True:
            instruction = f"{code[i]:05d}"
            mod_p2 = int(instruction[1])
            mod_p1 = int(instruction[2])
            op = int(instruction[3:])
            if op == 99:
                return result
            if op == 1:
                op1 = code[i + 1] if mod_p1 else code[code[i + 1]]
                op2 = code[i + 2] if mod_p2 else code[code[i + 2]]
                pointer = code[i + 3]
                code[pointer] = op1 + op2
                i += 4
            if op == 2:
                op1 = code[i + 1] if mod_p1 else code[code[i + 1]]
                op2 = code[i + 2] if mod_p2 else code[code[i + 2]]
                pointer = code[i + 3]
                code[pointer] = op1 * op2
                i += 4
            if op == 3:
                pointer = code[code[i + 1]] if mod_p1 else code[i + 1]
                code[pointer] = input_id
                i += 2
            if op == 4:
                pointer = code[code[i + 1]] if mod_p1 else code[i + 1]
                result = code[pointer]
                i += 2
            if op == 5:
                op1 = code[i + 1] if mod_p1 else code[code[i + 1]]
                op2 = code[i + 2] if mod_p2 else code[code[i + 2]]
                if op1 != 0:
                    i = op2
                    continue
                i += 3
            if op == 6:
                op1 = code[i + 1] if mod_p1 else code[code[i + 1]]
                op2 = code[i + 2] if mod_p2 else code[code[i + 2]]
                if op1 == 0:
                    i = op2
                    continue
                i += 3
            if op == 7:
                op1 = code[i + 1] if mod_p1 else code[code[i + 1]]
                op2 = code[i + 2] if mod_p2 else code[code[i + 2]]
                pointer = code[i + 3]
                code[pointer] = 1 if op1 < op2 else 0
                i += 4
            if op == 8:
                op1 = code[i + 1] if mod_p1 else code[code[i + 1]]
                op2 = code[i + 2] if mod_p2 else code[code[i + 2]]
                pointer = code[i + 3]
                code[pointer] = 1 if op1 == op2 else 0
                i += 4
