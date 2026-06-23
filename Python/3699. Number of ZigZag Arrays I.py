class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        if n == 1:
            return k
        
        dp_U = [v for v in range(k)]
        dp_D = [(k - 1 - v) for v in range(k)]
        
        for i in range(3, n + 1):
            next_U = [0] * k
            next_D = [0] * k
            
            curr_sum = 0
            for v in range(k):
                next_U[v] = curr_sum % MOD
                curr_sum += dp_D[v]
                
            curr_sum = 0
            for v in range(k - 1, -1, -1):
                next_D[v] = curr_sum % MOD
                curr_sum += dp_U[v]
                
            dp_U = next_U
            dp_D = next_D
            
        return (sum(dp_U) + sum(dp_D)) % MOD