class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        val_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            val_to_indices[val].append(i)
        
        result = [0] * len(nums)
        for indices in val_to_indices.values():
            n = len(indices)
            if n == 1: continue
            
            total_sum = sum(indices)
            left_sum = 0
            for i, idx in enumerate(indices):
                right_sum = total_sum - left_sum - idx
                result[idx] = (i * idx - left_sum) + (right_sum - (n - 1 - i) * idx)
                left_sum += idx
        return result