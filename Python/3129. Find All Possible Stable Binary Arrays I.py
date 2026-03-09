class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def dp(z, o, last):
            if z == 0 and o == 0:
                return 1
            
            res = 0
            if last == 0:
                for count in range(1, min(o, limit) + 1):
                    res = (res + dp(z, o - count, 1)) % MOD
            else:
                for count in range(1, min(z, limit) + 1):
                    res = (res + dp(z - count, o, 0)) % MOD
            return res

        total = 0
        for count in range(1, min(zero, limit) + 1):
            total = (total + dp(zero - count, one, 0)) % MOD
        for count in range(1, min(one, limit) + 1):
            total = (total + dp(zero, one - count, 1)) % MOD
            
        return total