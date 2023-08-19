class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        left_prefix_sum = self.prefix_sum[left]
        right_prefix_sum = self.prefix_sum[right + 1]

        return right_prefix_sum - left_prefix_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
