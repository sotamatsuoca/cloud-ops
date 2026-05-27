class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
            last_lower = {}
            first_upper = {}
            
            for i, char in enumerate(word):
                if char.islower():
                    last_lower[char] = i
                elif char.isupper() and char not in first_upper:
                    first_upper[char] = i
                    
            ans = 0
            for char in last_lower:
                up_char = char.upper()
                if up_char in first_upper and last_lower[char] < first_upper[up_char]:
                    ans += 1
                    
            return ans