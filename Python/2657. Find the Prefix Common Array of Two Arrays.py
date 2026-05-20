class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = []
        count = [0] * (n + 1)
        common_count = 0
        
        for a, b in zip(A, B):
            count[a] += 1
            if count[a] == 2:
                common_count += 1
            
            count[b] += 1
            if count[b] == 2:
                common_count += 1
            
            ans.append(common_count)
            
        return ans