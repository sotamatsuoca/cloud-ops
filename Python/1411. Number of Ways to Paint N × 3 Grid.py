class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        aba = 6
        abc = 6
        
        for _ in range(1, n):
            next_aba = (3 * aba + 2 * abc) % MOD
            next_abc = (2 * aba + 2 * abc) % MOD
            aba, abc = next_aba, next_abc
            
        return (aba + abc) % MOD