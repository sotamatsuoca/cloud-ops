class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sorted_nums = sorted(nums)
        
        groups = []
        num_to_group_idx = {}
        
        for num in sorted_nums:
            if not groups or num - groups[-1][-1] > limit:
                groups.append(collections.deque())
            groups[-1].append(num)
            num_to_group_idx[num] = len(groups) - 1
            
        result = []
        for num in nums:
            group_idx = num_to_group_idx[num]
            result.append(groups[group_idx].popleft())
            
        return result