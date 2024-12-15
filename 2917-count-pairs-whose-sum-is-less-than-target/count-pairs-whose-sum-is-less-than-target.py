class Solution(object):
    def countPairs(self, nums, target):
        left,right=0, len(nums)-1
        nums.sort()
        count=0
        while left<right:
            if nums[left]+nums[right]<target:
                count+= right-left
                left+=1
            else:
                right-=1
        return count
                
        