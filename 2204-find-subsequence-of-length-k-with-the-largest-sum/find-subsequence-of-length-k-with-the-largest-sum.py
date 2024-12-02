class Solution(object):
    def maxSubsequence(self, nums, k):
     
        indexed_nums = list(enumerate(nums))  
        k_largest = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]  
        
        k_largest_sorted = sorted(k_largest, key=lambda x: x[0])
        
       
        return [x[1] for x in k_largest_sorted]

