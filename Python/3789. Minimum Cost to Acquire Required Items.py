class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        m = min(need1, need2)
        option1 = need1 * cost1 + need2 * cost2
        option2 = m * costBoth + (need1 - m) * min(cost1, costBoth) + (need2 - m) * min(cost2, costBoth)
        option3 = max(need1, need2) * costBoth
        return min(option1, option2, option3)