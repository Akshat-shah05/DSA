class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = {}

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value
        
    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]
        
    def getValue(self, formula: str) -> int:
        part1, part2 = formula[1:].split('+')
        if part1 in self.cells:
            part1 = self.cells[part1]
        elif part1[0].isalpha():
            part1 = 0
        else:
            part1 = int(part1)
        if part2 in self.cells:
            part2 = self.cells[part2]
        elif part2[0].isalpha():
            part2 = 0
        else:
            part2 = int(part2)
        
        return part1 + part2
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)