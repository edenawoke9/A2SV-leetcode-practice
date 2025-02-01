class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        i=0
        j=0
        ans=""
        while i<len(word1) and j<len(word2):
            ans=ans+word1[i]+word2[j]
            i+=1
            j+=1
        ans=ans+ (word1[i:])
        ans=ans +(word2[j:])
        return ans



