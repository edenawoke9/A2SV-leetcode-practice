class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        num1 = "0" * (4 - len(str(num1))) + str(num1)
        num2 = "0" * (4 - len(str(num2))) + str(num2)  
        num3 = "0" * (4 - len(str(num3))) + str(num3)

        ans = ''.join(str(min(int(num1[i]), int(num2[i]), int(num3[i]))) for i in range(4))
        return int(ans) 
