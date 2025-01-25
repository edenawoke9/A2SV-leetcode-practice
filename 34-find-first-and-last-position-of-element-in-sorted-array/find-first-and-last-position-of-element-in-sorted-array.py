class Solution(object):
    def searchRange(self, nums, target):
       start=0
       end=len(nums)-1
       valuel=-1
       valuer=-1
       while end>=0:
        if nums[end]==target:
            valuer=end
            break 
        end-=1
       while start<=end:
        if nums[start]==target:
            valuel=start
            break 
        start+=1
       return [valuel,valuer]
        