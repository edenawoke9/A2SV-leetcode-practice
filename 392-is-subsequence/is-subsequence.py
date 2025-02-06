class Solution(object):
    #s="abc" t="ahbgdc" output=true
    def isSubsequence(self,s, t):
      j = 0 
      for char in t:  
        if j < len(s) and char == s[j]:  
            j += 1
      return j == len(s)  

