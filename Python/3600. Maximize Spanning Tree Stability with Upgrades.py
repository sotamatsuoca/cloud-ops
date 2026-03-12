class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges = []
        optional_edges = []
        for u, v, s, m in edges:
            if m == 1:
                must_edges.append((u, v, s))
            else:
                optional_edges.append((u, v, s))
        
        uf = UnionFind(n)
        min_must_strength = float('inf')
        
        for u, v, s in must_edges:
            if not uf.union(u, v):
                return -1
            min_must_strength = min(min_must_strength, s)
        
        optional_edges.sort(key=lambda x: x[2], reverse=True)
        
        included_optional_strengths = []
        
        for u, v, s in optional_edges:
            if uf.union(u, v):
                included_optional_strengths.append(s)
        
        if uf.count > 1:
            return -1
        
        included_optional_strengths.sort()
        
        for i in range(min(k, len(included_optional_strengths))):
            included_optional_strengths[i] *= 2
            
        min_optional_strength = min(included_optional_strengths) if included_optional_strengths else float('inf')
        
        return min(min_must_strength, min_optional_strength) if must_edges else min_optional_strength

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            self.count -= 1
            return True
        return False