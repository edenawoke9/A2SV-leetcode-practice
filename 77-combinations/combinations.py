from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
       
        result = []
        
        def backtrack(start: int, current_combination: List[int]):
     
            if len(current_combination) == k:
             
                result.append(current_combination[:])
                return

           
            for i in range(start, n + 1):
                
                current_combination.append(i)
               
                backtrack(i + 1, current_combination)
               
                current_combination.pop()

       
        backtrack(1, [])
        return result