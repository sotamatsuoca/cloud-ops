class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = bin(n)[2:]
        
        last_one_index = -1
        max_gap = 0
        
        for i, char in enumerate(binary_str):
            if char == '1':
                if last_one_index != -1:
                    max_gap = max(max_gap, i - last_one_index)
                
                last_one_index = i
                
        return max_gap