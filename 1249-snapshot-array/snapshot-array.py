class SnapshotArray:

    def __init__(self, length: int):
        self.snapId = 0
        self.snapArray = [[[-1, 0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        if self.snapArray[index][-1][0] == self.snapId:
            self.snapArray[index][-1][1] = val
        
        else:
            self.snapArray[index].append([self.snapId, val])
        
    def snap(self) -> int:
        snap = self.snapId
        self.snapId += 1
        return snap
        
    def get(self, index: int, snap_id: int) -> int:
        arr = self.snapArray[index]
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] == snap_id:
                return arr[mid][1]
            
            elif arr[mid][0] < snap_id:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return arr[r][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)