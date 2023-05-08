class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        # nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums

nums = [1,2,3,4,5,6,7]
k = 3
son = Solution().rotate(nums, k)
print(son)