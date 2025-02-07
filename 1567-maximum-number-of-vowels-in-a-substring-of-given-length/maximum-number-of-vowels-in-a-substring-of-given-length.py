class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        
        """
        self.s=s
        self.k=k
        countv=0
        maxV=0
        j=0
        
        vowels=['a','i','o','u','e']
        sett=[]
        while j<len(s):
            sett.append(s[j])
            if s[j] in vowels:
                countv+=1
            if len(sett)>=k:
                maxV=max(maxV,countv)
               
                if sett[0] in vowels:
                    countv-=1
                sett.remove(sett[0])
                
            j+=1
        return maxV


    