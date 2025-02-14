class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0 
        j = len(s) - 1
        s = list(s)  
   
        
        while i < j:
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i].isalpha() and not s[j].isalpha():
                j -= 1
            elif not s[i].isalpha() and s[j].isalpha():
                i += 1
            else: 
                i += 1
                j -= 1

        return "".join(s) 
