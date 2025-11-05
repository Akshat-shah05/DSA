class FileNode:
    def __init__(self):
        self.directories = {}
        self.files = {}

class FileSystem:

    def __init__(self):
        self.root = FileNode()
        self.root.directories["/"] = FileNode()
        
    def ls(self, path: str) -> List[str]:
        root = self.root.directories["/"]
        parts = path.split("/")

        if path == "/":
            return sorted(list(root.directories.keys()) + list(root.files.keys()))

        for part in parts[:-1]:
            if part == "":
                continue

            if part not in root.directories:
                return []
            
            root = root.directories[part]
        
        last = parts[-1]
        if last in root.files:
            return [last]
        
        if last not in root.directories:
            return []
        
        root = root.directories[last]
        return sorted(list(root.directories.keys()) + list(root.files.keys()))

    def mkdir(self, path: str) -> None:
        root = self.root.directories["/"]
        parts = path.split("/")

        for part in parts:
            if part == "":
                continue
            if part not in root.directories:
                root.directories[part] = FileNode()
            
            root = root.directories[part]

    def addContentToFile(self, filePath: str, content: str) -> None:
        root = self.root.directories["/"]
        parts = filePath.split("/")

        for part in parts[:-1]:
            if part == "":
                continue
            if part not in root.directories:
                root.directories[part] = FileNode()
            
            root = root.directories[part]

        root.files[parts[-1]] = root.files.get(parts[-1], "") + content

    def readContentFromFile(self, filePath: str) -> str:
        root = self.root.directories["/"]
        parts = filePath.split("/")

        for part in parts[:-1]:
            if part == "":
                continue
            if part not in root.directories:
                return ""
            
            root = root.directories[part]
        
        return root.files[parts[-1]]
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)