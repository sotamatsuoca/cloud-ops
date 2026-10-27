class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = []
        for i in range(m):
            if i == 0:
                row = '.' * n
            else:
                row = '#' * (n - 1) + '.'
            grid.append(row)
        return grid