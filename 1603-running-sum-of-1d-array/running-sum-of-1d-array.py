class Solution(object):
    def runningSum(self, nums):
       summ=0
       for i in range(len(nums)):
        summ=summ+nums[i]
        nums[i]=summ
       return nums
      
        