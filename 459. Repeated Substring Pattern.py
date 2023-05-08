class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        word = []
        l = len(s)
        for i in range(1, l+1):
            q = s[:i]
            if q == s[i:i+i]:
                word.append(q)
        long = 0
        for i in word:
            long = len(set(s.replace(i, '1', s.count(i))))
            if  long == 1:
                return True
        else:
            return False