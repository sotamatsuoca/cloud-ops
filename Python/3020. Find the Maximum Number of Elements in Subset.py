def maximumLength(nums: list[int]) -> int:
    freq = collections.Counter(nums)
    max_len = 1
    
    if 1 in freq:
        count_1 = freq[1]
        if count_1 % 2 == 0:
            count_1 -= 1
        max_len = max(max_len, count_1)
        
    for num in freq:
        if num == 1:
            continue
            
        current_len = 0
        curr = num
        
        while curr in freq:
            if freq[curr] >= 2:
                current_len += 2
                curr = curr * curr
            elif freq[curr] == 1:
                current_len += 1
                break
            else:
                break
                
        if curr not in freq and freq.get(int(math.isqrt(curr)), 0) >= 2:
             current_len -= 1

        max_len = max(max_len, current_len)
        
    return max_len