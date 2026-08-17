class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for idx in range(n):
            prefix[idx + 1] = prefix[idx] + stoneValue[idx]
        dp = [[0] * n for _ in range(n)]
        leftMax = [[0] * n for _ in range(n)]
        rightMax = [[0] * n for _ in range(n)]
        for i in range(n):
            leftMax[i][i] = stoneValue[i]
            rightMax[i][i] = stoneValue[i]
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                lo, hi = i, j - 1
                m = j
                while lo <= hi:
                    mid = (lo + hi) // 2
                    leftSum = prefix[mid + 1] - prefix[i]
                    rightSum = prefix[j + 1] - prefix[mid + 1]
                    if leftSum >= rightSum:
                        m = mid
                        hi = mid - 1
                    else:
                        lo = mid + 1
                ans = 0
                if m > i:
                    ans = max(ans, leftMax[i][m - 1])
                if m <= j - 1:
                    ans = max(ans, rightMax[m + 1][j])
                    leftSumM = prefix[m + 1] - prefix[i]
                    rightSumM = prefix[j + 1] - prefix[m + 1]
                    if leftSumM == rightSumM:
                        ans = max(ans, dp[i][m] + leftSumM)
                dp[i][j] = ans
                segSum = prefix[j + 1] - prefix[i]
                leftMax[i][j] = max(leftMax[i][j - 1], dp[i][j] + segSum)
                rightMax[i][j] = max(rightMax[i + 1][j], dp[i][j] + segSum)
        return dp[0][n - 1]