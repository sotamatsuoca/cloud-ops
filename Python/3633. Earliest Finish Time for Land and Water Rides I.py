class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calc(start1: List[int], dur1: List[int], start2: List[int], dur2: List[int]) -> int:
            min_end_first_stage = min(s + d for s, d in zip(start1, dur1))
            
            return min(max(s, min_end_first_stage) + d for s, d in zip(start2, dur2))
        
        land_then_water = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        
        water_then_land = calc(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(land_then_water, water_then_land)