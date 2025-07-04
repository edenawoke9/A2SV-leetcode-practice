from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        results = []

        def backtrack(start_index: int, current_combination: List[int], current_sum: int):
           
            if current_sum == target:
                results.append(current_combination[:])
                return

           
            if current_sum > target:
                return

           
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
               
                current_combination.append(candidate)
                
                
                backtrack(i, current_combination, current_sum + candidate)
                
                
                current_combination.pop()

        
        backtrack(0, [], 0)
        return results