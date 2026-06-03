class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def calc(start1: List[int], duration1: List[int], start2: List[int], duration2: List[int]) -> int:
            min_end_1 = min(s + d for s, d in zip(start1, duration1))
            
            return min(max(s, min_end_1) + d for s, d in zip(start2, duration2))
        
        option_land_first = calc(landStartTime, landDuration, waterStartTime, waterDuration)
        
        option_water_first = calc(waterStartTime, waterDuration, landStartTime, landDuration)
        
        return min(option_land_first, option_water_first)