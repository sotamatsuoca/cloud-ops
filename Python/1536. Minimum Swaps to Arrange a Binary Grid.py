class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ans = 0
        
        suffixZeros = [0] * n
        for i in range(n):
            count = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            suffixZeros[i] = count
            
        for i in range(n):
            neededZeros = n - 1 - i
            
            j = i
            while j < n and suffixZeros[j] < neededZeros:
                j += 1
                
            if j == n:
                return -1
                
            while j > i:
                suffixZeros[j], suffixZeros[j-1] = suffixZeros[j-1], suffixZeros[j]
                ans += 1
                j -= 1
                
        return ans