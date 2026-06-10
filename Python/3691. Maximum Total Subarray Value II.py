class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        max_power = n.bit_length()
        st_max = [[0] * max_power for _ in range(n)]
        st_min = [[0] * max_power for _ in range(n)]
        
        for i in range(n):
            st_max[i][0] = nums[i]
            st_min[i][0] = nums[i]
            
        for j in range(1, max_power):
            for i in range(n - (1 << j) + 1):
                st_max[i][j] = max(st_max[i][j-1], st_max[i + (1 << (j-1))][j-1])
                st_min[i][j] = min(st_min[i][j-1], st_min[i + (1 << (j-1))][j-1])
                
        def query_val(l, r):
            if l > r:
                return 0
            length = r - l + 1
            j = length.bit_length() - 1
            mx = max(st_max[l][j], st_max[r - (1 << j) + 1][j])
            mn = min(st_min[l][j], st_min[r - (1 << j) + 1][j])
            return mx - mn

        heap = []
        for i in range(n):
            val = query_val(i, n - 1)
            heapq.heappush(heap, (-val, i, n - 1))
            
        total_value = 0
        for _ in range(k):
            if not heap:
                break
            neg_val, l, r = heapq.heappop(heap)
            total_value += (-neg_val)
            
            if l < r:
                val_left = query_val(l, r - 1)
                heapq.heappush(heap, (-val_left, l, r - 1))
                
        return total_value