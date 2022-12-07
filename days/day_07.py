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


LIMIT_DISK_SPACE = 70000000
UPDATE_MINIMUM_SPACE = 30000000


class Day07:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.sizes: list[list[int]] = []

    def part_one(self) -> int:
        root = self._build_tree()
        self._calculate_sizes(root)
        result = []
        for size in self.sizes:
            result.extend([sum(s for s in size if s <= 100000)])
        return sum(result)

    def part_two(self) -> int:
        root = self._build_tree()
        self._calculate_sizes(root)
        unused_space = LIMIT_DISK_SPACE - root.size
        needed_space = UPDATE_MINIMUM_SPACE - unused_space
        result = []
        for sizes in self.sizes:
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
                new_dir = self._create_directory_from_line(line, current_directory)
                current_directory.directories[new_dir.name] = new_dir
                continue
            current_directory.files.append(self._create_file_from_line(line))
        return root

    @staticmethod
    def _create_directory_from_line(
        line: str, current_directory: Directory
    ) -> Directory:
        name = line.split("dir ")[1]
        return Directory(name=name, parent=current_directory)

    @staticmethod
    def _create_file_from_line(line: str) -> File:
        size, name = line.split(" ")
        return File(name=name, size=int(size))

    def _calculate_sizes(self, root: Directory) -> None:
        for child in root.directories.values():
            self._walk(child, [root.size, child.size])

    def _walk(self, directory: Directory, acc: list[int]) -> list[int]:
        if not directory.directories:
            self.sizes.append(acc)
            return acc
        for child in directory.directories.values():
            self._walk(child, [*acc, child.size])
        return acc
