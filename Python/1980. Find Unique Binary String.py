class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i, s in enumerate(nums):
            ans.append("1" if s[i] == "0" else "0")
        return "".join(ans)