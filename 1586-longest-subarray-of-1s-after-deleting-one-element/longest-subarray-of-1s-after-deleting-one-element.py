class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        i=0
        count=0
        maxv=0
        while j<len(nums):
            if nums[j]==0:
                count+=1
            while count>1:
                if nums[i]==0:
                    count-=1
                
                i+=1
            maxv=max(maxv,j-i)
            j+=1
        return maxv
        