class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j

        for a, b in allowedSwaps:
            union(a, b)

        groups = defaultdict(Counter)
        for i in range(n):
            groups[find(i)][source[i]] += 1

        hamming_distance = 0
        for i in range(n):
            root = find(i)
            val = target[i]
            if groups[root][val] > 0:
                groups[root][val] -= 1
            else:
                hamming_distance += 1

        return hamming_distance