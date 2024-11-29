class Solution(object):
    def maxScore(self, cardPoints, k):
        n = len(cardPoints)  
        current_sum = sum(cardPoints[:k])
        maxx = current_sum  
        for i in range(1, k + 1):  
            current_sum -= cardPoints[k - i]
           
            current_sum += cardPoints[n - i]
            
            
            maxx = max(maxx, current_sum)
        
       
        return maxx
