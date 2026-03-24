class Solution:
    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        result = [[0] * cols for _ in range(rows)]
        MOD = 12345

        suffix_prod = 1
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                result[r][c] = suffix_prod
                suffix_prod = (suffix_prod * grid[r][c]) % MOD

        prefix_prod = 1
        for r in range(rows):
            for c in range(cols):
                result[r][c] = (result[r][c] * prefix_prod) % MOD
                prefix_prod = (prefix_prod * grid[r][c]) % MOD
        return result