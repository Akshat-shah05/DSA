from typing import List

class FileNode:
    def __init__(self):
        self.childDirectories = {}
        self.files = {}

class FileSystem:

    def __init__(self):
        self.fs = FileNode()
        self.fs.childDirectories["/"] = FileNode()

    def _root(self) -> FileNode:
        return self.fs.childDirectories["/"]

    def _parts(self, path: str) -> List[str]:
        return [p for p in path.split("/") if p]

    def ls(self, path: str) -> List[str]:
        node = self._root()
        if path == "/":
            return sorted(list(node.childDirectories.keys()) + list(node.files.keys()))

        parts = self._parts(path)

        for i, name in enumerate(parts):
            is_last = (i == len(parts) - 1)
            if is_last and name in node.files:
                return [name]
            if name not in node.childDirectories:
                return []
            node = node.childDirectories[name]

        return sorted(list(node.childDirectories.keys()) + list(node.files.keys()))

    def mkdir(self, path: str) -> None:
        node = self._root()
        for name in self._parts(path):
            if name not in node.childDirectories:
                node.childDirectories[name] = FileNode()
            node = node.childDirectories[name]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._root()
        parts = self._parts(filePath)
        for name in parts[:-1]:
            if name not in node.childDirectories:
                node.childDirectories[name] = FileNode()
            node = node.childDirectories[name]
        fname = parts[-1]
        node.files[fname] = node.files.get(fname, "") + content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._root()
        parts = self._parts(filePath)
        for name in parts[:-1]:
            node = node.childDirectories[name]
        fname = parts[-1]
        return node.files[fname]
