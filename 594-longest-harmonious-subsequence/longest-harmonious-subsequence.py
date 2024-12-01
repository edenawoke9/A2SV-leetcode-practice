from collections import Counter

class Solution:
    def findLHS(self, nums):
        count = Counter(nums)  
        x = 0
        for num in count:
            if num + 1 in count:  
                x = max(x, count[num] + count[num + 1])  
        return x
