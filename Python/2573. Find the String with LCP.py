class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        s = [0] * n
        char_code = ord('a')
        
        for i in range(n):
            if s[i] == 0:
                if char_code > ord('z'):
                    return ""
                s[i] = char_code
                for j in range(i + 1, n):
                    if lcp[i][j] > 0:
                        s[j] = char_code
                char_code += 1
        
        res = "".join(chr(c) if c != 0 else '' for c in s)
        if len(res) < n or 0 in s:
            for i in range(n):
                if s[i] == 0: return ""
            res = "".join(chr(c) for c in s)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                length = 0
                if i < n and j < n:
                    if res[i] == res[j]:
                        length = 1 + (lcp[i+1][j+1] if i+1 < n and j+1 < n else 0)
                
                if lcp[i][j] != length:
                    return ""
                    
        return res