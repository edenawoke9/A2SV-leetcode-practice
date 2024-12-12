class Solution(object):
    def countGoodSubstrings(self,s):
         j=0
         i=3
         count=0
         while i<=len(s):
            if len(s[j:i])==len(set(s[j:i])):
              count+=1
            i+=1
            j+=1
         return count
      