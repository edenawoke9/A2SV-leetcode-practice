class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        i=0
        while i<len(nums):
            if nums[i]==original:
                original*=2
            i+=1
        return original 
        