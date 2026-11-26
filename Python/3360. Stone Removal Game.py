class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 0
        remove = 10
        while remove > 0 and n >= remove:
            n -= remove
            remove -= 1
            turn += 1
        return turn % 2 == 1