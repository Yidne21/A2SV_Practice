class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        for i in range(len(nums) - 1):
            ans.append(ans[i] + nums[i + 1])

        return ans 
