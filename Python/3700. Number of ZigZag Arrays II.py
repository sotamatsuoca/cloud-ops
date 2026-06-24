class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        if n == 1:
            return k
        if n == 2:
            return (k * (k - 1)) % MOD
            
        dim = 2 * k
        T = [[0] * dim for _ in range(dim)]
        
        for i in range(k):
            for j in range(i):
                T[k + j][i] = 1
            for j in range(i + 1, k):
                T[j][k + i] = 1
                
        init = [0] * dim
        for j in range(k):
            init[j] = j
            init[k + j] = k - 1 - j
            
        def multiply(A, B):
            C = [[0] * dim for _ in range(dim)]
            for i in range(dim):
                for k_idx in range(dim):
                    if A[i][k_idx] == 0:
                        continue
                    for j in range(dim):
                        C[i][j] = (C[i][j] + A[i][k_idx] * B[k_idx][j]) % MOD
            return C

        def power(A, p):
            res = [[0] * dim for _ in range(dim)]
            for i in range(dim):
                res[i][i] = 1
            base = A
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res

        T_pow = power(T, n - 2)
        
        ans = 0
        for i in range(dim):
            row_sum = 0
            for j in range(dim):
                row_sum = (row_sum + T_pow[i][j] * init[j]) % MOD
            ans = (ans + row_sum) % MOD
            
        return ans