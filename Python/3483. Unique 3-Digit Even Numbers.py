class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        results = set()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        if digits[i] != 0 and digits[k] % 2 == 0:
                            number = digits[i] * 100 + digits[j] * 10 + digits[k]
                            results.add(number)
        return len(results)