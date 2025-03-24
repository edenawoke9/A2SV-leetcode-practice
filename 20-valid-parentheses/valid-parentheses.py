class Solution:
    def isValid(self, s: str) -> bool:
        array = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char not in mapping:  
                array.append(char)
            else:  
                if not array or array[-1] != mapping[char]:
                    return False
                array.pop()  
        
        return not array
