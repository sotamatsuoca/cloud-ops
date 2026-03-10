class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
      
        @cache
        def count_arrays(zeros_left: int, ones_left: int, last_digit: int) -> int:
            if zeros_left == 0:
                return int(last_digit == 1 and ones_left <= limit)
          
            if ones_left == 0:
                return int(last_digit == 0 and zeros_left <= limit)
          
            if last_digit == 0:
                total = count_arrays(zeros_left - 1, ones_left, 0) + count_arrays(zeros_left - 1, ones_left, 1)
              
                if zeros_left - limit - 1 >= 0:
                    total -= count_arrays(zeros_left - limit - 1, ones_left, 1)
              
                return total
          
            else:
                total = count_arrays(zeros_left, ones_left - 1, 0) + count_arrays(zeros_left, ones_left - 1, 1)
              
                if ones_left - limit - 1 >= 0:
                    total -= count_arrays(zeros_left, ones_left - limit - 1, 0)
              
                return total
      
        result = (count_arrays(zero, one, 0) + count_arrays(zero, one, 1)) % MOD
      
        count_arrays.cache_clear()
      
        return result