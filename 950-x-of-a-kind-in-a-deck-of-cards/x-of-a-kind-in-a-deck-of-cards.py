from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        values = Counter(deck).values()
        min_count = min(values)  

        for x in range(2, min_count + 1):  
            if all(count % x == 0 for count in values):  
                return True  
        return False  
