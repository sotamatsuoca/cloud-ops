class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        flat = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                idx = (i * n + j + k) % (m * n)
                flat[idx] = grid[i][j]
        result = []
        for i in range(m):
            result.append(flat[i * n:(i + 1) * n])
        return result