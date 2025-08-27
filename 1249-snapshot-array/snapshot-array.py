class SnapshotArray:

    def __init__(self, length: int):
        self.snapId = -1
        self.snapArray = [[(-1, 0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        arr = self.snapArray[index]
        if arr[-1][0] == self.snapId + 1:
            arr[-1] = (self.snapId + 1, val)
        
        else:
            arr.append((self.snapId + 1, val))

    def snap(self) -> int:
        self.snapId += 1
        return self.snapId
        

    def get(self, index: int, snap_id: int) -> int:
        arr = self.snapArray[index]
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] <= snap_id:
                l = mid + 1
            else:
                r = mid - 1
        
        return arr[r][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)