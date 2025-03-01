from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_value = 0
        for s in strs:
      
            if s.isdigit():
                max_value = max(max_value, int(s))
            else:
                max_value = max(max_value, len(s))
        return max_value

