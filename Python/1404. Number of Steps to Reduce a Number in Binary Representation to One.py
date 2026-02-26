class Solution(object):
    def numSteps(self, s: str) -> int:
        result, carry = 0, 0
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:
                carry = 1
                result += 2
            else:
                result += 1
        
        return result + carry
