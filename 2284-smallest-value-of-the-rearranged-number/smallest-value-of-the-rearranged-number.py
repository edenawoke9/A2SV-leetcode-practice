class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        is_negative = num < 0
        num = abs(num)
        num = list(str(num))
        
        if is_negative:
           
            num.sort(reverse=True)
            return -int("".join(num))
        else:
          
            num.sort()
           
            if num[0] == '0':
                for i in range(1, len(num)):
                    if num[i] != '0':
                        num[0], num[i] = num[i], num[0]
                        break
            return int("".join(num))


