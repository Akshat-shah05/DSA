class SnapshotArray:

    def __init__(self, length: int):
        self.snapArr = [[[0, 0]] for _ in range(length)]
        self.id = 0

    def set(self, index: int, val: int) -> None:
        if self.snapArr[index][-1][0] == self.id:
            self.snapArr[index][-1] = [self.id, val]
        else:
            self.snapArr[index].append([self.id, val])

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, index: int, snap_id: int) -> int:
        snapIndex = bisect_right(self.snapArr[index], snap_id, key=lambda x: x[0])
        return self.snapArr[index][snapIndex - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)