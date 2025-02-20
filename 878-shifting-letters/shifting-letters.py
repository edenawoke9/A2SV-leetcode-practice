class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s=list(s)
        total_sum=0
        
       
    
        for i in range (len(s)-1,-1,-1):
            total_sum+=shifts[i]
            s[i] = chr(((ord(s[i]) - ord('a') + total_sum) % 26) + ord('a'))
            
        return "".join(s)
        