class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp = t
        for p in [2, 3, 5, 7]:
            while temp % p == 0:
                temp //= p
        if temp > 1:
            return "-1"
        
        n = len(num)
        s = list(num)
        for i in range(n):
            if s[i] == '0':
                s[i] = '1'
                for j in range(i + 1, n):
                    s[j] = '1'
                break
                
        def check(rem_t, length):
            if rem_t == 1:
                return True
            for d in range(9, 1, -1):
                while rem_t % d == 0 and length > 0:
                    rem_t //= d
                    length -= 1
                if rem_t == 1:
                    return True
            return rem_t == 1

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        left_t = [1] * (n + 1)
        left_t[0] = t
        for i in range(n):
            d = int(s[i])
            left_t[i+1] = left_t[i] // gcd(left_t[i], d)
            
        if left_t[n] == 1:
            return "".join(s)
            
        for i in range(n - 1, -1, -1):
            start_d = int(s[i]) + 1
            for d in range(start_d, 10):
                next_t = left_t[i] // gcd(left_t[i], d)
                if check(next_t, n - 1 - i):
                    s[i] = str(d)
                    cur_t = next_t
                    for j in range(n - 1, i, -1):
                        for d_fill in range(9, 0, -1):
                            if cur_t % d_fill == 0 and check(cur_t // d_fill, j - 1 - i):
                                s[j] = str(d_fill)
                                cur_t //= d_fill
                                break
                        else:
                            s[j] = '1'
                    return "".join(s)
                    
        ans_digits = []
        cur_t = t
        for d in range(9, 1, -1):
            while cur_t % d == 0:
                ans_digits.append(str(d))
                cur_t //= d
        while len(ans_digits) <= n:
            ans_digits.append('1')
        ans_digits.sort()
        return "".join(ans_digits)