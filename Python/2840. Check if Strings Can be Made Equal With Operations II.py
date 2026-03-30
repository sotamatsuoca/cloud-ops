class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        count_even = collections.Counter()
        count_odd = collections.Counter()
        
        for i in range(len(s1)):
            if i % 2 == 0:
                count_even[s1[i]] += 1
                count_even[s2[i]] -= 1
            else:
                count_odd[s1[i]] += 1
                count_odd[s2[i]] -= 1
                
        return all(freq == 0 for freq in count_even.values()) and \
               all(freq == 0 for freq in count_odd.values())