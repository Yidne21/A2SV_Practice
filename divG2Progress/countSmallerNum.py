class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(nums)
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if i != j:
                    if nums[i] > nums[j]:
                        cnt += 1
            ans[i] = cnt
        return ans

