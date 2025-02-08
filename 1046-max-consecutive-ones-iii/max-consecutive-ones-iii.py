class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        j=0
        i=0
        count=0
        maxv=0
        while j<len(nums):
            if nums[j]==0:
                count+=1
          
            while count>k:
                if nums[i]==0:
                    count-=1
                i+=1
            maxv=max(maxv,j-i+1)
            j+=1
        return maxv
                

        