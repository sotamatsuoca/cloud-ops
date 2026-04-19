class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = max_dist = 0
        m, n = len(nums1), len(nums2)
        
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1
                
        return max_dist