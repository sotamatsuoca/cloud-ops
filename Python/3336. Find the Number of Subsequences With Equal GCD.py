class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAXV = 200

        def mobius_sieve(n):
            mu = [1] * (n + 1)
            is_prime = [True] * (n + 1)
            primes = []
            mu[0] = 0
            for i in range(2, n + 1):
                if is_prime[i]:
                    primes.append(i)
                    mu[i] = -1
                for p in primes:
                    if i * p > n:
                        break
                    is_prime[i * p] = False
                    if i % p == 0:
                        mu[i * p] = 0
                        break
                    else:
                        mu[i * p] = -mu[i]
            return mu

        MU = mobius_sieve(MAXV)

        n = len(nums)
        freq = [0] * (MAXV + 1)
        for v in nums:
            freq[v] += 1

        C = [0] * (MAXV + 1)
        for k in range(1, MAXV + 1):
            s = 0
            for m in range(k, MAXV + 1, k):
                s += freq[m]
            C[k] = s

        pow2 = [1] * (n + 1)
        pow3 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD
            pow3[i] = pow3[i - 1] * 3 % MOD

        ans = 0
        for g in range(1, MAXV + 1):
            if C[g] < 2:
                continue
            D = MAXV // g
            if D < 1:
                continue

            def cntp(d, g=g, D=D, C=C):
                if d > D:
                    return 0
                k = g * d
                if k > MAXV:
                    return 0
                return C[k]

            answer_g = 0
            for d1 in range(1, D + 1):
                mu1 = MU[d1]
                if mu1 == 0:
                    continue
                c1 = cntp(d1)
                for d2 in range(1, D + 1):
                    mu2 = MU[d2]
                    if mu2 == 0:
                        continue
                    c2 = cntp(d2)
                    gg = math.gcd(d1, d2)
                    lcm = d1 // gg * d2
                    n_both = cntp(lcm) if lcm <= D else 0
                    exp2 = c1 + c2 - 2 * n_both
                    W_all = pow3[n_both] * pow2[exp2] % MOD
                    W_Aempty = pow2[c2]
                    W_Bempty = pow2[c1]
                    W_nonempty = (W_all - W_Aempty - W_Bempty + 1) % MOD
                    answer_g = (answer_g + mu1 * mu2 * W_nonempty) % MOD
            ans = (ans + answer_g) % MOD
        return ans % MOD