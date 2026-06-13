class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            weight = sum(weights[ord(char) - ord('a')] for char in word)
            
            mod = weight % 26
            
            mapped_char = chr(ord('z') - mod)
            res.append(mapped_char)
            
        return "".join(res)