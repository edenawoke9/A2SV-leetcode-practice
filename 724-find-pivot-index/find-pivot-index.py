class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leftsum=0
        rightsum=sum(nums)
        ans=[0]*(len(nums)+2)
        for j in range(1,len(nums)+1):
            ans[j]=nums[j-1]
            leftsum=leftsum+ans[j-1]
            rightsum-=ans[j-1]
            if leftsum==(rightsum-ans[j]):
                return  j-1
        return -1
                                                      

            
        