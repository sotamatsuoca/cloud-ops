class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        ans = 0
        
        for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase):
            if lower in char_set and upper in char_set:
                ans += 1
                
        return ans