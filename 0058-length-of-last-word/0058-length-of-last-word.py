class Solution(object):
    def lengthOfLastWord(self, s):
        text = s.split()
        x = text.pop(-1)
        return len(x)