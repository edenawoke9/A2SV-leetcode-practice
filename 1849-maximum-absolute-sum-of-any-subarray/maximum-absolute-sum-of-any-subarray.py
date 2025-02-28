class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_so_far=0
        max_ending_here=0
        min_so_far=(10**5)
        min_ending_here=(10**5)
        for num in nums:
            max_ending_here=max(num,max_ending_here+num)
            max_so_far=max(max_so_far,max_ending_here)
            min_ending_here=min(num,min_ending_here+num)
            min_so_far=min(min_so_far,min_ending_here)
        return max(abs(min_so_far),max_so_far)

        