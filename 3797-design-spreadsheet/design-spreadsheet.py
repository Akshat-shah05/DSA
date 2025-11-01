class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        column = cell[0]
        row = int(cell[1:])

        self.grid[row - 1][ord(column) - ord("A")] = value
        
    def resetCell(self, cell: str) -> None:
        column = cell[0]
        row = int(cell[1:])

        self.grid[row - 1][ord(column) - ord("A")] = 0

    def getValue(self, formula: str) -> int:
        elem1, elem2 = formula[1:].split("+")
        elem1val, elem2val = 0, 0
        
        if elem1[0].isalpha():
            column = elem1[0]
            row = int(elem1[1:])

            elem1val = self.grid[row - 1][ord(column) - ord("A")]
        
        else:
            elem1val = int(elem1)
        
        if elem2[0].isalpha():
            column = elem2[0]
            row = int(elem2[1:])

            elem2val = self.grid[row - 1][ord(column) - ord("A")]
        
        else:
            elem2val = int(elem2)

        return elem1val + elem2val

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)