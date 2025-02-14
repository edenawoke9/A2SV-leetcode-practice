class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums=nums
        count=0
        k=1
        i=1
        
        while i<len(nums):
            k+=1
            if nums[i-1]==nums[i]:
                count+=1
                if count==2:
                    del nums[i]
                    count-=1
                    k-=1
                else:
                    i+=1
            else:
                count=0
                i+=1
        return k
