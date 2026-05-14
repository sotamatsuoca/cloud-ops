class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        if n == 0: return False
        
        cnt = Counter(nums)
        
        if cnt[n] != 2:
            return False
        
        for i in range(1, n):
            if cnt[i] != 1:
                return False
                
        return True