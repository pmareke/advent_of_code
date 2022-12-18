from dataclasses import dataclass


@dataclass
class Day05:
    lines: list[str]

    def part_one(self) -> int:
        letters = self.lines[0]
        return self._destroy(letters)

    def part_two(self) -> int:
        letters = self.lines[0]
        unique = set(letters.lower())
        sizes: list[int] = []
        for letter in unique:
            translations = {ord(letter): "", ord(letter.upper()): ""}
            letter = letters.translate(translations)
            sizes.append(self._destroy(letter))
        return min(sizes)

    @staticmethod
    def _destroy(letters: str) -> int:
        stack: list[str] = []
        for letter in letters:
            if stack and abs(ord(letter) - ord(stack[-1])) == 32:
                stack.pop()
                continue
            stack.append(letter)
        return len(stack)
