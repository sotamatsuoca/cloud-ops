class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z0 = s.count('0')
        if z0 == 0: return 0
        
        unvisited = [set(), set()]
        for i in range(n + 1):
            if i != z0:
                unvisited[i % 2].add(i)
        
        evens = sorted([i for i in range(n + 1) if i % 2 == 0 and i != z0])
        odds = sorted([i for i in range(n + 1) if i % 2 != 0 and i != z0])
        avail = [evens, odds]
        
        queue = deque([(z0, 0)])
        
        while queue:
            z, ops = queue.popleft()
            
            low = abs(z - k)
            high = n - abs(n - z - k)
            
            target_list = avail[low % 2]
            
            left_idx = bisect.bisect_left(target_list, low)
            right_idx = bisect.bisect_right(target_list, high)
            
            if left_idx < right_idx:
                to_visit = target_list[left_idx:right_idx]
                
                target_list[left_idx:right_idx] = []
                
                for next_z in to_visit:
                    if next_z == 0:
                        return ops + 1
                    queue.append((next_z, ops + 1))
                    
        return -1