from typing import List

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        
        value_map = {ch: vals[i] for i, ch in enumerate(chars)}
      
        arr = [value_map.get(ch, ord(ch) - ord('a') + 1) for ch in s]
        
      
        max_cost, current_sum = 0, 0
        for val in arr:
            current_sum = max(val, current_sum + val)
            max_cost = max(max_cost, current_sum)
        
        return max_cost

