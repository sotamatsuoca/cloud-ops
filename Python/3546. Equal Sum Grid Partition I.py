class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total_sum = sum(sum(row) for row in grid)
        
        if total_sum % 2 != 0:
            return False
        
        current_sum = 0
        for i in range(len(grid) - 1):
            current_sum += sum(grid[i])
            if current_sum * 2 == total_sum:
                return True
        
        current_sum = 0
        cols = list(zip(*grid))
        for j in range(len(cols) - 1):
            current_sum += sum(cols[j])
            if current_sum * 2 == total_sum:
                return True
        
        return False