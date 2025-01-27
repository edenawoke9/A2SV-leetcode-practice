class Solution(object):
    def minSubArrayLen(self, target, nums):
        start = 0
        end = 0
        sum = 0
        minlen = float('inf')

        while end < len(nums):  
            sum += nums[end]

        
            while sum >= target:
                minlen = min(minlen, end - start + 1)  
                sum -= nums[start]
                start += 1

            end += 1  

       
        return minlen if minlen != float('inf') else 0
