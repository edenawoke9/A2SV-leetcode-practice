class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        self.version1=version1
        self.version2=version2
        
        v1 = version1.split(".")

        
        v2=version2.split(".")
        print(v1,v2)
        maxlen=max(len(v1),len(v2))
        v1.extend(["0"]*(maxlen-len(v1)))
        v2.extend(["0"]*(maxlen-len(v2)))
        print(v1,v2)
        i=0
        while i<maxlen:
         if int(v1[i])>int(v2[i]):
            return 1
         if int(v2[i])>int(v1[i]):
            return -1
         i+=1
        
        return 0


       
       
       

      
        


      
        
