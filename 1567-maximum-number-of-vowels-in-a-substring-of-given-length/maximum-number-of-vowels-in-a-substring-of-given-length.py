class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        
        """
        self.s=s
        self.k=k
        vowels=['a','i','o','u','e']
        countv=sum([1 for i in range (k) if s[i] in vowels])
        
        maxv=countv
       
        for j in range(k,len(s)):
            if s[j] in vowels:
                countv+=1
            if s[j-k] in vowels:
                countv-=1
            maxv=max(maxv,countv)
        return maxv


    