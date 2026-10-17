class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        order = sorted(range(n), key=lambda i: (digit_sum(nums[i]), nums[i]))
        
        visited = [False] * n
        swaps = 0
        for i in range(n):
            if visited[i] or order[i] == i:
                continue
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = order[j]
                cycle_len += 1
            swaps += cycle_len - 1
        
        return swaps