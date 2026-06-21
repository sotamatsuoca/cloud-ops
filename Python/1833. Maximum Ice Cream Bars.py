class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        ice_cream_count = 0
        
        for cost in costs:
            if coins >= cost:
                coins -= cost
                ice_cream_count += 1
            else:
                break
                
        return ice_cream_count