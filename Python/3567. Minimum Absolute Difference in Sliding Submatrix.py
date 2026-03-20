class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                nums = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        nums.append(grid[x][y])

                nums.sort()

                d = float('inf')
                for a, b in pairwise(nums):
                    if a != b:
                        d = min(d, abs(a - b))
                
                ans[i][j] = d if d != float('inf') else 0

        return ans