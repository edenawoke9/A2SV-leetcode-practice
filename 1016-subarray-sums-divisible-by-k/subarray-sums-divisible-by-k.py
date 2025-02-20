class Solution(object):
    def subarraysDivByK(self, nums, k):
        
        
         count=0
         summ=0
         dic={0: 1}
         for i in range(len(nums)):
            summ+=nums[i]
            reminder=summ%k
            if reminder<0:
                reminder+=k
            count+=dic.get(reminder,0)
            dic[reminder]=dic.get(reminder,0)+1
         return count

