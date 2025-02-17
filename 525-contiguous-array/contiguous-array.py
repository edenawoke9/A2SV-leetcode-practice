class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {0: -1}  
        balance = 0 
        maxV = 0  

        for i, num in enumerate(nums):
            balance += 1 if num == 1 else -1  
            
            if balance in dic:
                maxV = max(maxV, i - dic[balance])  
            else:
                dic[balance] = i  
        
        return maxV
