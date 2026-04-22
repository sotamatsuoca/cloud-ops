class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        result = []
        for query in queries:
            for word in dictionary:
                diffs = sum(1 for a, b in zip(query, word) if a != b)
                
                if diffs <= 2:
                    result.append(query)
                    break
        return result