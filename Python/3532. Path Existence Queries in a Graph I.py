class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                group[i] = group[i - 1] + 1
            else:
                group[i] = group[i - 1]

        answer = []
        for u, v in queries:
            answer.append(group[u] == group[v])

        return answer