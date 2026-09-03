class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        count_odd = 0
        min_odd = None
        min_even = None
        for x in nums1:
            if x % 2 == 1:
                count_odd += 1
                if min_odd is None or x < min_odd:
                    min_odd = x
            else:
                if min_even is None or x < min_even:
                    min_even = x
        count_even = len(nums1) - count_odd
        target_even_ok = (count_odd == 0)
        target_odd_ok = (count_even == 0) or (count_odd > 0 and min_odd < min_even)
        return target_even_ok or target_odd_ok