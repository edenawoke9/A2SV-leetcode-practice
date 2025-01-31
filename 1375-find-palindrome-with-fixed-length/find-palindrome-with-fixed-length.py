class Solution(object):
    def kthPalindrome(self, queries, intLength):
        self.queries = queries
        self.intLength = intLength
        returnv = []

        for k in queries:
            ans = [0] * intLength
            half_len = (intLength + 1) // 2
            min_half = 10**(half_len - 1)
            half_num = min_half + (k - 1)

            if half_num >= 10**half_len:
                returnv.append(-1)
                continue

            half_str = str(half_num)
            for i in range(half_len):
                ans[i] = int(half_str[i])

            for i in range(intLength - half_len):
                ans[intLength - 1 - i] = ans[i]

            returnv.append(int("".join(map(str, ans))))
        
        return returnv
