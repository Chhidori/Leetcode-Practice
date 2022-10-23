class Solution:
    def isPalindrome(self, x):
      x = str(x)
      if x[::-1]==x:
       return True
        