class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = []
        l2 = []
        for i in set(nums):
            l.append(nums.count(i))
            l2.append(i)
        return l2[l.index(min(l))]