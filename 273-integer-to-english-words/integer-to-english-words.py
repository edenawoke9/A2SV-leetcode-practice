class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        # Helper arrays for number to word mappings
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", 
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", 
               "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
        
        def helper(n):
            if n == 0:
                return ""
            elif n < 10:
                return ones[n] + " "
            elif n < 20:
                return teens[n - 10] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return ones[n // 100] + " Hundred " + helper(n % 100)
        
        res = ""
        i = 0
        
        while num > 0:
            chunk = num % 1000
            if chunk != 0:
                res = helper(chunk) + thousands[i] + " " + res
            num = num // 1000
            i += 1
        
        return res.strip()