class Solution(object):
    def climbStairs(self, n):
        x = 1
        y = 1
        while n!= 1:
            temp = x
            x = x + y
            y = temp
            n-=1
        return x    
        