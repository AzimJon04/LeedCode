class Solution:
    def reverseWords(self, s: str) -> str:
        new = ''
        for word in s.split():
           new += word[::-1] + " "
        new = new.rstrip()
        return new