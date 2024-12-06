class Solution(object):
    
        def sortedSquares(self, nums):
              nums=[abs(x)**2 for x in nums]
              
              return sorted(nums)
              
        