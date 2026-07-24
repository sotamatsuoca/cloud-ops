class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        distinct = sorted(set(nums))
        n = len(distinct)
        pair_xor = set()
        for i in range(n):
            for j in range(i, n):
                pair_xor.add(distinct[i] ^ distinct[j])
        result = set()
        for p in pair_xor:
            for c in distinct:
                result.add(p ^ c)
        return len(result)