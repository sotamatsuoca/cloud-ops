class Solution:
    def minOperations(self, s: str) -> int:
        count1 = 0
        for i, c in enumerate(s):
            if c != '01'[i & 1]: 
                count1 += 1
        
        count2 = len(s) - count1

        return min(count1, count2)