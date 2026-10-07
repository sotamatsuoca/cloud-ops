class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_remove = 0
        right_remove = 0
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()
        path = []

        def dfs(index, left_count, right_count, left_rem, right_rem):
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            if ch == '(' and left_rem > 0:
                dfs(index + 1, left_count, right_count, left_rem - 1, right_rem)
            elif ch == ')' and right_rem > 0:
                dfs(index + 1, left_count, right_count, left_rem, right_rem - 1)

            path.append(ch)
            if ch != '(' and ch != ')':
                dfs(index + 1, left_count, right_count, left_rem, right_rem)
            elif ch == '(':
                dfs(index + 1, left_count + 1, right_count, left_rem, right_rem)
            elif right_count < left_count:
                dfs(index + 1, left_count, right_count + 1, left_rem, right_rem)
            path.pop()

        dfs(0, 0, 0, left_remove, right_remove)
        return list(result)