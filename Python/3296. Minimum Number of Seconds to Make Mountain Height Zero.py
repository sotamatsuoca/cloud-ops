class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def check(t: int) -> bool:
            h = 0
            for wt in workerTimes:
                h += int((math.sqrt(1 + 8 * t / wt) - 1) / 2)
            return h >= mountainHeight

        low = 0
        high = min(workerTimes) * (mountainHeight * (mountainHeight + 1)) // 2
        
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans