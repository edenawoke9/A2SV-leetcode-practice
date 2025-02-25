class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        index=nums.index(max(nums))
        nums.sort(reverse=True)
        if nums[0]/2 >=nums[1]:
            return index
        else:
            return -1
        