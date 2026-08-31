class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        idx = 1
        first = -1
        last = -1
        min_dist = float('inf')
        while curr.next:
            if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
                if first == -1:
                    first = idx
                else:
                    min_dist = min(min_dist, idx - last)
                last = idx
            prev = curr
            curr = curr.next
            idx += 1
        if first == -1 or first == last:
            return [-1, -1]
        return [min_dist, last - first]