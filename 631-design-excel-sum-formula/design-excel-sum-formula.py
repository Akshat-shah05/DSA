class Excel:

    def __init__(self, height: int, width: str):
        self.H = height
        self.W = ord(width) - ord('A') + 1
        self.val = [[0] * (self.W + 1) for _ in range(self.H + 1)]
        self.formula = {} # (r, c) -> Formula
        self.rev = defaultdict(set) # set of (r, c) that depend on (r2, c2)
    
    def _col(self, ch):
        return ord(ch) - ord('A') + 1
    
    def _expand(self, tokens):
        out = Counter()
        for t in tokens:
            if ":" not in t:
                c, r = self._col(t[0]), int(t[1:])
                out[(r, c)] += 1

            else:
                a, b = t.split(":")
                c1, r1 = self._col(a[0]), int(a[1:])
                c2, r2 = self._col(b[0]), int(b[1:])
                if r1 > r2: r1, r2 = r2, r1
                if c1 > c2: c1, c2 = c2, c1
                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        out[(r, c)] += 1
        
        return out
    
    def _recompute(self, cell):
        # recompute cell from its formula (if any)
        if cell not in self.formula: return
        total = 0
        for (r2, c2), k in self.formula[cell].items():
            total += self.val[r2][c2] * k
        r, c = cell
        self.val[r][c] = total

    def _propagate(self, start):
        q = deque([start])
        while q:
            u = q.popleft()
            for v in list(self.rev[u]):
                self._recompute(v)
                q.append(v)
    
    def _detach_formula(self, cell):
        if cell in self.formula:
            for ref in self.formula[cell]:
                self.rev[ref].discard(cell)
            del self.formula[cell]


    def set(self, row: int, column: str, val: int) -> None:
        cell = (row, self._col(column))
        self._detach_formula(cell)
        self.val[row][self._col(column)] = val
        self._propagate(cell)

    def get(self, row: int, column: str) -> int:
        return self.val[row][self._col(column)]

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cell = (row, self._col(column))
        refs = self._expand(numbers)

        self._detach_formula(cell)
        self.formula[cell] = refs
        for ref in refs:
            self.rev[ref].add(cell)
        
        self._recompute(cell)
        self._propagate(cell)
        return self.val[row][self._col(column)]



# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)