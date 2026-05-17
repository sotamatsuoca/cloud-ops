class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if 0 <= start < len(arr) and arr[start] >= 0:
            if arr[start] == 0:
                return True
            
            jump = arr[start]
            arr[start] = -arr[start]
            
            return self.canReach(arr, start + jump) or self.canReach(arr, start - jump)
            
        return False