class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        
        ans = []
        for perm in set(permutations(nums)):  
            ans.append(list(perm))
        
        return ans
