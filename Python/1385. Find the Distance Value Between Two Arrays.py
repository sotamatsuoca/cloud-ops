class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        arr2 = sorted(arr2)
        n = len(arr2)
        count = 0

        for x in arr1:
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if arr2[mid] < x:
                    left = mid + 1
                else:
                    right = mid

            nearest = float('inf')
            if left < n:
                nearest = min(nearest, abs(arr2[left] - x))
            if left > 0:
                nearest = min(nearest, abs(arr2[left - 1] - x))

            if nearest > d:
                count += 1

        return count