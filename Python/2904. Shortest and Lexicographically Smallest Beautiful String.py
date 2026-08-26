class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        ans = ""
        min_len = n + 1
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                if sub.count('1') == k:
                    curr_len = len(sub)
                    if curr_len < min_len:
                        min_len = curr_len
                        ans = sub
                    elif curr_len == min_len:
                        if sub < ans:
                            ans = sub
                            
        return ans