class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        base = 2**(n - 1)
        
        if k > 3 * base:
            return ""
        
        result = []
        first_char_index = (k - 1) // base
        result.append(chr(ord('a') + first_char_index))
        
        k -= first_char_index * base
        
        while base > 1:
            base //= 2
            if (k - 1) // base == 0:
                if result[-1] != 'a':
                    result.append('a')
                else:
                    result.append('b')
            else:
                if result[-1] != 'c':
                    result.append('c')
                else:
                    result.append('b')
                k -= base
                
        return "".join(result)