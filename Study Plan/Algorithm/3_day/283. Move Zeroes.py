class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1 and 0 in nums:
            n = nums.count(0)
            o = [0]*n
            while 0 in nums:
                nums.remove(0)
            return nums.extend(o)
        else:
            nums