class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count_waviness_up_to(N: int) -> int:
            if N <= 0:
                return 0
            
            s = str(N)
            L = len(s)
            memo = {}
            
            def dp(idx, prev2, prev, is_less, is_started):
                if idx == L:
                    return 1, 0
                
                state = (idx, prev2, prev, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = 9 if is_less else int(s[idx])
                res_count = 0
                res_waviness = 0
                
                for d in range(limit + 1):
                    next_less = is_less or (d < limit)
                    
                    if not is_started:
                        if d == 0:
                            c, w = dp(idx + 1, -1, -1, next_less, False)
                        else:
                            c, w = dp(idx + 1, -1, d, next_less, True)
                    else:
                        is_waviness = 0
                        if prev2 != -1:
                            if (prev > prev2 and prev > d) or (prev < prev2 and prev < d):
                                is_waviness = 1
                        
                        c, w = dp(idx + 1, prev, d, next_less, True)
                        w += is_waviness * c
                    
                    res_count += c
                    res_waviness += w
                
                memo[state] = (res_count, res_waviness)
                return memo[state]
            
            return dp(0, -1, -1, False, False)[1]

        return count_waviness_up_to(num2) - count_waviness_up_to(num1 - 1)