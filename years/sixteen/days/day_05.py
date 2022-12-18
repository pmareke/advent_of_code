import hashlib
from dataclasses import dataclass


@dataclass
class Day05:
    lines: list[str]

    def part_one(self) -> str:
        secret_key = self.lines[0]
        result = ""
        number = 0
        for _ in range(8):
            while True:
                number += 1
                md5 = hashlib.md5(f"{secret_key}{number}".encode())
                password = md5.hexdigest()
                if password.startswith("0" * 5):
                    result += password[5]
                    break
        return result

    def part_two(self) -> str:
        secret_key = self.lines[0]
        result = ["_" for _ in range(8)]
        number = 0
        for _ in range(8):
            while True:
                number += 1
                md5 = hashlib.md5(f"{secret_key}{number}".encode())
                password = md5.hexdigest()
                if password.startswith("0" * 5):
                    index = int(password[5], 16)
                    if index < 8:
                        if result[int(index)] == "_":
                            result[int(index)] = md5.hexdigest()[6]
                            break
        return "".join(result)
