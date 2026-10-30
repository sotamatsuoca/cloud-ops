class Solution:
    def shortestPath(self, n: int, edges: list[list[int]], labels: str, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            
        distances = {}
        start_char = labels[0]
        distances[(0, start_char, 1)] = 0
        
        pq = [(0, 0, start_char, 1)]
        
        while pq:
            d, u, curr_char, curr_count = heapq.heappop(pq)
            
            if u == n - 1:
                return d
                
            if d > distances.get((u, curr_char, curr_count), float('inf')):
                continue
                
            for v, w in adj[u]:
                nxt_char = labels[v]
                nxt_count = (curr_count + 1) if nxt_char == curr_char else 1
                
                if nxt_count > k:
                    continue
                    
                nxt_dist = d + w
                state = (v, nxt_char, nxt_count)
                
                if nxt_dist < distances.get(state, float('inf')):
                    distances[state] = nxt_dist
                    heapq.heappush(pq, (nxt_dist, v, nxt_char, nxt_count))
                    
        return -1