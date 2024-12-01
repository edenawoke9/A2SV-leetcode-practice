class Solution(object):
    def minimumRecolors(self, blocks, k):
       self.blocks=blocks
       self.k=k
       currentCount=blocks[:k].count("W")
       minimum=currentCount
       i=1
       while i<=len(blocks)-k:
           if blocks[i-1]=="W":
               currentCount-=1
           if blocks[k+i-1]=="W":
               currentCount+=1
           minimum=min (minimum,currentCount)
           i+=1
       return minimum

        
    