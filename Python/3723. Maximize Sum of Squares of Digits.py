class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        nines, rest = divmod(sum, 9)
        result = "9" * nines
        if rest:
            result += str(rest)
        return result + "0" * (num - len(result))