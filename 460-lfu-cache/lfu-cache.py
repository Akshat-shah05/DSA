class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {}
        self.freq2key = defaultdict(OrderedDict)
        self.minf = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        
        oldFreq = self.key2freq[key]
        self.key2freq[key] = oldFreq + 1
        self.freq2key[oldFreq].pop(key)
        if not self.freq2key[oldFreq]:
            del self.freq2key[oldFreq]
        
        self.freq2key[oldFreq + 1][key] = 1
        while self.minf not in self.freq2key:
            self.minf += 1
        
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if key in self.key2val:
            self.get(key)
            self.key2val[key] = value
            return 
        
        if len(self.key2val) == self.cap:
            deleted_item, _ = self.freq2key[self.minf].popitem(last=False)
            del self.key2val[deleted_item]
            del self.key2freq[deleted_item]
        
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.minf = 1
        self.freq2key[self.minf][key] = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)