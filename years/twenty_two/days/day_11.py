from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: list[int]
    operation: Callable
    divisible_by: int
    true_monkey: int
    false_monkey: int
    inspected_items: int = 0


class MonkeyFactory:
    @staticmethod
    def create_monkey(section: str) -> Monkey:
        lines = section.split("\n")
        items = [lines[1].split("Starting items: ")[1].split(", ")]
        callback = lines[2].split("Operation: new = ")[1]
        operation = lambda old: eval(callback)
        divisible_by = int(lines[3].split()[-1])
        true_monkey = int(lines[4].split()[-1])
        false_monkey = int(lines[5].split()[-1])
        return Monkey(
            list(map(int, *items)),
            operation,
            divisible_by,
            true_monkey,
            false_monkey,
        )


@dataclass
class Day11:
    lines: list[str]

    def part_one(self) -> int:
        return self._play_rounds(rounds=20)

    def part_two(self) -> int:
        return self._play_rounds(rounds=10000)

    def _play_rounds(self, rounds: int) -> int:
        monkeys = self._create_monkeys()
        iteration = 0
        while iteration < rounds:
            iteration += 1
            self._play_round(monkeys, bool(rounds == 20))
        items = sorted([monkey.inspected_items for monkey in monkeys])
        return items[-1] * items[-2]

    def _create_monkeys(self) -> list[Monkey]:
        monkeys: list[Monkey] = []
        for section in "\n".join(self.lines).split("\n\n"):
            monkeys.append(MonkeyFactory.create_monkey(section))
        return monkeys

    def _play_round(self, monkeys: list[Monkey], part_two: bool) -> None:
        less_common_divisor = self._find_less_common_divisor(monkeys)
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspected_items += 1
                if part_two:
                    new_worry_level = monkey.operation(item) // 3
                else:
                    new_worry_level = monkey.operation(item) % less_common_divisor
                if new_worry_level % monkey.divisible_by == 0:
                    monkeys[monkey.true_monkey].items.append(new_worry_level)
                else:
                    monkeys[monkey.false_monkey].items.append(new_worry_level)
            monkey.items = []

    @staticmethod
    def _find_less_common_divisor(monkeys: list[Monkey]) -> int:
        less_common_divisor = 1
        for monkey in monkeys:
            less_common_divisor *= less_common_divisor * monkey.divisible_by
        return less_common_divisor
