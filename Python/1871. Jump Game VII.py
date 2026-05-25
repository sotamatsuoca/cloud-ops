class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        dp = [True] + [False] * (n - 1)
        count = 0
        
        for i in range(1, n):
            if i >= minJump:
                count += dp[i - minJump]
            if i > maxJump:
                count -= dp[i - maxJump - 1]
                
            dp[i] = (count > 0) and (s[i] == '0')
            
        return dp[n - 1]