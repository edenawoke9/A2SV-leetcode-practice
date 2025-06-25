from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot_index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot_index = i
                break
        if pivot_index == -1:
            nums.reverse()
            return
        for i in range(n - 1, pivot_index, -1):
            if nums[i] > nums[pivot_index]:
                nums[pivot_index], nums[i] = nums[i], nums[pivot_index]
                break
        left, right = pivot_index + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1