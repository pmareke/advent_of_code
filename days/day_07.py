from collections import defaultdict
from dataclasses import dataclass
from typing import Optional


@dataclass
class File:
    size: int
    name: str


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"] = None) -> None:
        self.name = name
        self.parent = parent
        self.files: list[File] = []
        self.directories: dict[str, "Directory"] = defaultdict()

    @property
    def size(self) -> int:
        file_size = sum(file.size for file in self.files)
        sizes = [child.size for child in self.directories.values()]
        return file_size + sum(sizes)

    def __repr__(self) -> str:
        return f"name={self.name}, directories={self.directories}"


class Day07:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.total: list[int] = []
        self.total2: list[list[int]] = []

    def part_one(self) -> int:
        root = self._build_tree()
        self._calculate_sizes(root)
        return sum(self.total)

    def part_two(self) -> int:
        root = self._build_tree()
        self._calculate_sizes(root)
        unused_space = 70000000 - root.size
        needed_space = 30000000 - unused_space
        result = []
        for sizes in self.total2:
            result.extend([size for size in sizes if size > needed_space])
        return int(sorted(result)[0])

    def _build_tree(self) -> Directory:
        root = Directory(name="/")
        current_directory = root
        for line in self.lines[1:]:
            assert current_directory
            if line == "$ ls":
                continue
            if line == "$ cd ..":
                assert current_directory.parent
                current_directory = current_directory.parent
                continue
            if line.startswith("$ cd "):
                name = line.split("$ cd ")[1]
                current_directory = current_directory.directories[name]
                continue
            if line.startswith("dir "):
                new_dir = self._create_directory_from_line(line)
                new_dir.parent = current_directory
                current_directory.directories[new_dir.name] = new_dir
                continue
            current_directory.files.append(self._create_file_from_line(line))
        return root

    @staticmethod
    def _create_file_from_line(line: str) -> File:
        size, name = line.split(" ")
        return File(name=name, size=int(size))

    @staticmethod
    def _create_directory_from_line(line: str) -> Directory:
        name = line.split("dir ")[1]
        return Directory(name)

    def _calculate_sizes(self, root: Directory) -> None:
        sizes = [root.size]
        for child in root.directories.values():
            self._walk(child, [*sizes, child.size])

    def _walk(self, directory: Directory, acc: list[int]) -> list[int]:
        if not directory.directories:
            self.total.append(sum(s for s in acc if s <= 100000))
            self.total2.append(acc)
            return acc
        for child in directory.directories.values():
            self._walk(child, [*acc, child.size])
        return acc
