class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s=s
        words=s.split()
        l=0
        r=len(words)-1
     
        while l<=r:
            words[r],words[l]=words[l],words[r]
            
            l+=1
            r-=1
        return " ".join(words)

       
