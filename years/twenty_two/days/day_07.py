from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Day07:
    lines: list[str]

    def part_one(self) -> int:
        tree = self._build_tree()
        return sum(size for size in tree.values() if size < 100000)

    def part_two(self) -> int:
        limit_disk_space = 70000000
        update_minimum_space = 30000000
        tree = self._build_tree()
        needed_space = tree["/"] - (limit_disk_space - update_minimum_space)
        valid_paths = [path for path in tree.values() if path >= needed_space]
        return sorted(valid_paths)[0]

    def _build_tree(self) -> dict[str, int]:
        tree: dict[str, int] = defaultdict(int)
        stack: list[str] = []
        for line in self.lines:
            if line == "$ ls" or line.startswith("dir"):
                continue
            if line == "$ cd ..":
                stack.pop()
                continue
            if line.startswith("$ cd "):
                path = line.split("$ cd ")[1]
                stack.append(path)
                continue
            size = line.split(" ")[0]
            for i in range(1, len(stack) + 1):
                tree["/".join(stack[:i])] += int(size)
        return tree
