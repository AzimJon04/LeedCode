# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i, m = 1, n
        while i < m:
            k = (i + m)//2
            if isBadVersion(k):
                m = k
            else:
                i = k + 1
        return i
    