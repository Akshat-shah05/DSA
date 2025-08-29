class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""

        values = self.timeMap[key]
        if not values:
            return ""

        l = 0
        r = len(self.timeMap[key]) - 1

        while l <= r:
            mid = (l + r) // 2
            ts = values[mid][1]

            if ts == timestamp:
                return values[mid][0]

            elif ts < timestamp:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return values[r][0] if r >= 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)