class Solution(object):
    def reverseVowels(self, s):
        self.s=s
        l=0
        r=len(s)-1
        s=list(s)
        array=['a', 'e', 'i', 'o','u','A','E','I','O','U']
        while l<r:
            if s[l] in array and s[r] in array:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            elif s[l] in array and s[r] not in array:
                r-=1 
            elif s[l] not in array and s[r]  in array:
                l+=1
            else:
                l+=1
                r-=1
        return ''.join(s)
        