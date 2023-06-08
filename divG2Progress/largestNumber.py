class Solution(object):
    def largestNumber(self, nums):
        if not any(nums):
            return '0'
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                order1 = int(str(nums[i]) + str(nums[j]))
                order2 = int(str(nums[j]) + str(nums[i]))
                if order1 > order2:
                    pass
                elif order2 > order1:
                    nums[i], nums[j] = nums[j], nums[i]
        return ''.join(str(i) for i in nums)

