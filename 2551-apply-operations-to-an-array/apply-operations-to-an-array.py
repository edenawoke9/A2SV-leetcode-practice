class Solution(object):
    def applyOperations(self, nums):
         for i in range(len(nums)-1):
           if nums[i]==nums[i+1]:
               nums[i]=2*nums[i]
               nums[i+1]=0
         k=0
         i=1
         while(i<len(nums)):
            if nums[k]==0:
               if nums[i]!=0:
                  nums[k],nums[i]=nums[i],nums[k]
               else:
                  i+=1
            else:
                 k+=1
                 i+=1
         return nums
        