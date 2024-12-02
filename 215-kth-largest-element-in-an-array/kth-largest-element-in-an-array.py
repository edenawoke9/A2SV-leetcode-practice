class Solution(object):
    def findKthLargest(self, nums, k):
        self.nums = nums
        self.k = k
        nums.sort(reverse=True)
        return nums[k-1]
        
        