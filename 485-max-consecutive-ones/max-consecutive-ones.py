class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
       self.nums=nums
       
       current_len=0 
       length=0
       for i in nums:
           
          if i==1:
             current_len+=1
          else:
             current_len=0
          length=max(length,current_len)
       return length
           
               