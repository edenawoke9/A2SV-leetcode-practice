class Solution(object):
    def missingNumber(self, nums):
        result=[0]*(len(nums)+1)
        for i in range(len(nums)+1):
            result[i]=i
        return sum(result)-sum(nums)
