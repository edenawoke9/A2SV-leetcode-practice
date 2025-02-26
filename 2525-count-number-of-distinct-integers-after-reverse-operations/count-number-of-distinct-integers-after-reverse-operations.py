

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set()
        
        def reverse(num):
            num = str(num)
            num = list(num)
            i = 0
            j = len(num) - 1  
            while i < j:  
                num[i], num[j] = num[j], num[i]
                i += 1
                j -= 1
            return int("".join(num))
        
        for num in nums:
            ans.add(num)
            ans.add(reverse(num))  
        
        return len(ans)
