class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False
        