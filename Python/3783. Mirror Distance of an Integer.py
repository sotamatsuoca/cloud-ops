class Solution:
    def mirrorDistance(self, n: int) -> int:
        original_n = n
        reversed_n = 0
        
        temp_n = n
        while temp_n > 0:
            digit = temp_n % 10
            reversed_n = reversed_n * 10 + digit
            temp_n //= 10
            
        return abs(original_n - reversed_n)