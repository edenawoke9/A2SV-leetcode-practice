class Solution(object):
    
   def findShortestSubArray(self, nums):
       
        dic={}
        first={}
        last={}
        minn=float("inf")
        for i in range(len(nums)):
            if nums[i] not in dic:
                    first[nums[i]]=i
                    dic[nums[i]]=1
            last[nums[i]]=i
            dic[nums[i]]+=1
            degree=max(dic.values())
        for i in dic:
            if dic[i]==degree:
                minn=min(minn,(last[i]-first[i]+1))
        return minn

        
        
        
        