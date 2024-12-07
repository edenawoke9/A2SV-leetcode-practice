class Solution(object):
    def findContentChildren(self, g, s):
        i=0
        j=0
        count=0
        g.sort()
        s.sort()
        while i<len(g)and j<len(s):
            if s[j]>=g[i]:
                count+=1
                i+=1
            j+=1
        return count
           
        