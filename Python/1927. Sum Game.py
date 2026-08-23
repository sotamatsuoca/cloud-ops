class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        sum1 = sum2 = cnt1 = cnt2 = 0
        for i in range(n // 2):
            c = num[i]
            if c == '?':
                cnt1 += 1
            else:
                sum1 += int(c)
        for i in range(n // 2, n):
            c = num[i]
            if c == '?':
                cnt2 += 1
            else:
                sum2 += int(c)
        cnt = cnt1 + cnt2
        if cnt % 2 == 1:
            return True
        return sum1 - sum2 != (cnt2 - cnt1) // 2 * 9