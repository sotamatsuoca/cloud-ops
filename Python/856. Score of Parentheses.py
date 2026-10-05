class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                inner = stack.pop()
                value = 1 if inner == 0 else 2 * inner
                stack[-1] += value
        return stack[0]