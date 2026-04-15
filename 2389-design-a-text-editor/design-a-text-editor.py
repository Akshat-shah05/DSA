from collections import deque

class TextEditor:

    def __init__(self):
        self.leftOfCursor = deque()
        self.rightOfCursor = deque()

    def addText(self, text: str) -> None:
        for char in text:
            self.leftOfCursor.append(char)
        
    def deleteText(self, k: int) -> int:
        deleted = 0
        for _ in range(k):
            if self.leftOfCursor:
                self.leftOfCursor.pop()
                deleted += 1
        
        return deleted

    def last10(self) -> str:
        chars = list(islice(reversed(self.leftOfCursor), 10))
        chars.reverse()
        return "".join(chars)

    def cursorLeft(self, k: int) -> str:
        for _ in range(min(k, len(self.leftOfCursor))):
            self.rightOfCursor.appendleft(self.leftOfCursor.pop())
        return self.last10()

    def cursorRight(self, k: int) -> str:
        for _ in range(min(k, len(self.rightOfCursor))):
            self.leftOfCursor.append(self.rightOfCursor.popleft())
        return self.last10()

        


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)