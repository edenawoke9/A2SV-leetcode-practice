class Solution(object):
    def isSubsequence(self, s, t):
        m=0
        n=0
        while m<len(s) and n<len(t):
           if s[m]==t[n]:
               m+=1
           n+=1
        return m==len(s)
        