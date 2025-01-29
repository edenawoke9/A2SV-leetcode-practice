class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        min_sum = float('inf') 
        for length in range(l, r + 1):
           
            for i in range(len(nums) - length + 1): 
                subarray_sum = sum(nums[i:i+length]) 
                if subarray_sum > 0:
                    min_sum = min(min_sum, subarray_sum)  
      
        return min_sum if min_sum != float('inf') else -1
