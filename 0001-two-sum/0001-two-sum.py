class Solution(object):
    def twoSum(self, nums, target):
     n = len(nums)
     for i in range(n):
      for j in range(i+1,n):
        if nums[j]== target-nums[i]:
          return [i,j]