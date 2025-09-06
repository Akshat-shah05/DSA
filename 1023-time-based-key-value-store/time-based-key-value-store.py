class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        l, r = 0, len(self.timeMap[key]) - 1
        toSearch = self.timeMap[key]

        while l <= r:
            mid = (l + r) // 2
            if toSearch[mid][0] < timestamp:
                l = mid + 1
            
            elif toSearch[mid][0] == timestamp:
                return toSearch[mid][1]
            
            else:
                r = mid - 1
        
        return toSearch[r][1] if r >= 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)