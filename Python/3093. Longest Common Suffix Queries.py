class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = {}
        
        def get_better(idx1, idx2):
            if idx1 == -1: return idx2
            len1, len2 = len(wordsContainer[idx1]), len(wordsContainer[idx2])
            if len1 < len2: return idx1
            if len2 < len1: return idx2
            return min(idx1, idx2)

        global_best = 0
        for i in range(1, len(wordsContainer)):
            global_best = get_better(global_best, i)
        root["best"] = global_best
        
        for i, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr:
                    curr[char] = {"best": i}
                curr = curr[char]
                curr["best"] = get_better(curr["best"], i)
        
        ans = []
        for query in wordsQuery:
            curr = root
            res = root["best"]
            for char in reversed(query):
                if char in curr:
                    curr = curr[char]
                    res = curr["best"]
                else:
                    break
            ans.append(res)
            
        return ans