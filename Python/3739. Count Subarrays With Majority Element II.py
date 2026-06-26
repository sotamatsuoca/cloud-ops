class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        sl = SortedList([0])
        prefix_counts = {0: 1}
        pref = 0
        total_subarrays = 0
        
        for num in nums:
            if num == target:
                pref += 1
            else:
                pref -= 1
                
            idx = sl.bisect_left(pref)
            total_subarrays += idx
            
            sl.add(pref)
            prefix_counts[pref] = prefix_counts.get(pref, 0) + 1
            
        return total_subarrays