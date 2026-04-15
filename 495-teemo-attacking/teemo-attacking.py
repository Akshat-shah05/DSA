class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] > duration:
                poisoned += duration
            
            else:
                poisoned += timeSeries[i] - timeSeries[i - 1]

        poisoned += duration
        return poisoned
        