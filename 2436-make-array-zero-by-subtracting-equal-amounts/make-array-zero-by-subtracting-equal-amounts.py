class Solution(object):
    def minimumOperations(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                count += 1
                subtract_value = nums[i]
                for j in range(i, len(nums)):
                    nums[j] -= subtract_value
        return count
