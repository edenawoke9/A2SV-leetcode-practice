class Solution:
    def findLHS(self, nums):
        nums.sort() 
        start = 0
        max_length = 0

        for end in range(len(nums)):
            
            while nums[end] - nums[start] > 1:
                start += 1

           
            if nums[end] - nums[start] == 1:
                max_length = max(max_length, end - start + 1)  #
        return max_length


