class Solution(object):
    def mostFrequentEven(self, nums):
       self.nums=nums
       nums.sort()
       maxx=0
       value=-1
       for i in range(len(nums)):
           if nums[i]%2==0:
               if nums.count(nums[i])>maxx:
                   maxx=nums.count(nums[i])
                   value=nums[i]
                
       return value
