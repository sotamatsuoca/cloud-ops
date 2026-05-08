class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        max_val = max(nums)
        
        is_prime = [True] * (max_val + 1)
        is_prime[0] = is_prime[1] = False
        for p in range(2, int(max_val**0.5) + 1):
            if is_prime[p]:
                for i in range(p * p, max_val + 1, p):
                    is_prime[i] = False
        
        val_to_indices = {}
        for idx, val in enumerate(nums):
            if val not in val_to_indices:
                val_to_indices[val] = []
            val_to_indices[val].append(idx)
            
        queue = deque([(0, 0)])
        visited_indices = {0}
        visited_primes = set()
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            if curr_idx == n - 1:
                return steps
            
            for next_idx in [curr_idx - 1, curr_idx + 1]:
                if 0 <= next_idx < n and next_idx not in visited_indices:
                    if next_idx == n - 1: return steps + 1
                    visited_indices.add(next_idx)
                    queue.append((next_idx, steps + 1))
            
            val = nums[curr_idx]
            if is_prime[val] and val not in visited_primes:
                visited_primes.add(val)
                for multiple in range(val, max_val + 1, val):
                    if multiple in val_to_indices:
                        for next_idx in val_to_indices[multiple]:
                            if next_idx not in visited_indices:
                                if next_idx == n - 1: return steps + 1
                                visited_indices.add(next_idx)
                                queue.append((next_idx, steps + 1))
                        del val_to_indices[multiple]
                        
        return -1