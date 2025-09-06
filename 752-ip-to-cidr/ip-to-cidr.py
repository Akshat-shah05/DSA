class Solution:
    def ipToInt(self, ip):
        a, b, c, d = map(int, ip.split("."))
        return (a << 24) | (b << 16) | (c << 8) | d
    
    def intToIp(self, x):
        a, b, c, d = (x >> 24) & 0x000000FF, (x >> 16) & 0x000000FF, (x >> 8) & 0x000000FF, (x >> 0) & 0x000000FF
        arr = [str(a), str(b), str(c), str(d)]
        return '.'.join(arr)

    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        start = self.ipToInt(ip)
        ans = []
        while n:
            align_mask = 0 if start == 0 else 33 - ((start & -start).bit_length())
            # size constraint
            size_mask = 33 - n.bit_length()
            mask = max(align_mask, size_mask)

            step = 1 << (32 - mask)           # safe: 32 - mask >= 0
            ans.append(f"{self.intToIp(start)}/{mask}")
            start += step
            n -= step
        
        return ans


        