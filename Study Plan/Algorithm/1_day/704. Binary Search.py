class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            return -1

nums = [-1,0,3,5,9,12]
target = 9
b = Solution()
b.search(nums, target)
print(b.search(nums, target))