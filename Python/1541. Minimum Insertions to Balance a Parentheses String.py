class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need = 0
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '(':
                if need % 2 == 1:
                    insertions += 1
                    need -= 1
                need += 2
                i += 1
            else:
                need -= 1
                if need < 0:
                    insertions += 1
                    need += 2
                i += 1
        return insertions + need