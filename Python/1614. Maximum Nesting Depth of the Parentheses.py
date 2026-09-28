class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        result = 0
        for ch in s:
            if ch == '(':
                depth += 1
                if depth > result:
                    result = depth
            elif ch == ')':
                depth -= 1
        return result