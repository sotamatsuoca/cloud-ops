class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(x: int) -> int:
            product = 1
            while x > 0:
                product *= x % 10
                x //= 10
            return product

        candidate = n
        while digitProduct(candidate) % t != 0:
            candidate += 1
        return candidate