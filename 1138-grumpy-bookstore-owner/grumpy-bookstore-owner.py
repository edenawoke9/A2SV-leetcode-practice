from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
       
        baseline = 0
        for i in range(n):
            if grumpy[i] == 0:
                baseline += customers[i]
        
       
        max_additional = 0
        current_additional = 0
        
        
        for i in range(minutes):
            if grumpy[i] == 1:
                current_additional += customers[i]
        max_additional = current_additional
       
        for i in range(minutes, n):
            
            left = i - minutes
            if grumpy[left] == 1:
                current_additional -= customers[left]
          
            if grumpy[i] == 1:
                current_additional += customers[i]
            
            max_additional = max(max_additional, current_additional)
        
        
        return baseline + max_additional