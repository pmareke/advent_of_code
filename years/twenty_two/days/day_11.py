from dataclasses import dataclass
from typing import Callable


@dataclass
class Monkey:
    items: list[int]
    operation: Callable
    divisible_by: int
    test: Callable
    true_monkey: int
    false_monkey: int
    inspected_items: int = 0

    def add_item(self, item: int) -> None:
        self.items.append(item)


@dataclass
class Day11:
    lines: list[str]

    def part_one(self) -> int:
        monkeys = self._create_monkeys()
        iteration = 0
        while iteration < 20:
            iteration += 1
            for monkey in monkeys:
                for item in monkey.items:
                    monkey.inspected_items += 1
                    new_worry_level = monkey.operation(item) // 3
                    destination = (
                        monkey.true_monkey
                        if monkey.test(new_worry_level)
                        else monkey.false_monkey
                    )
                    monkeys[destination].add_item(new_worry_level)
                monkey.items = []
        inspected_items = sorted(
            [monkey.inspected_items for monkey in monkeys], reverse=True
        )
        return inspected_items[0] * inspected_items[1]

    def part_two(self) -> int:
        monkeys = self._create_monkeys()
        iteration = 0
        less_common_divisor = self._find_less_common_divisor(monkeys)
        while iteration < 10000:
            iteration += 1
            for monkey in monkeys:
                for item in monkey.items:
                    monkey.inspected_items += 1
                    new_worry_level = monkey.operation(item) % less_common_divisor
                    destination = (
                        monkey.true_monkey
                        if monkey.test(new_worry_level)
                        else monkey.false_monkey
                    )
                    monkeys[destination].add_item(new_worry_level)
                monkey.items = []
        inspected_items = sorted(
            [monkey.inspected_items for monkey in monkeys], reverse=True
        )
        return inspected_items[0] * inspected_items[1]

    def _create_monkeys(self) -> list[Monkey]:
        monkeys: list[Monkey] = []
        for section in "\n".join(self.lines).split("\n\n"):
            monkeys.append(self._create_monkey(section))
        return monkeys

    @staticmethod
    def _create_monkey(section: str) -> Monkey:
        lines = section.split("\n")
        items = [
            int(number) for number in lines[1].split("Starting items: ")[1].split(", ")
        ]
        callback = lines[2].split("Operation: new = ")[1]
        operation = lambda old: eval(callback)
        divisible_by = lines[3].split("Test: divisible by ")[1]
        test = lambda old: old % int(divisible_by) == 0
        true_monkey = lines[4].split("If true: throw to monkey ")[1]
        false_monkey = lines[5].split("If false: throw to monkey ")[1]
        return Monkey(
            items,
            operation,
            int(divisible_by),
            test,
            int(true_monkey),
            int(false_monkey),
        )

    @staticmethod
    def _find_less_common_divisor(monkeys: list[Monkey]) -> int:
        less_common_divisor = 1
        for monkey in monkeys:
            less_common_divisor *= less_common_divisor * monkey.divisible_by
        return less_common_divisor
