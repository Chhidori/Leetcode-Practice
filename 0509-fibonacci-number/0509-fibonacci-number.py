class Solution(object):
    def fib(self, n):
        if n==0:
            return(0)
        elif n==1:
            return(1)
        else:
            temp = 0
            x = 0
            y = 1
            while n > 1:
                temp = x + y
                x = y
                y = temp
                n-=1

            return(temp) 
            