class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + arr[i]

        total = 0
        for length in range(1, n + 1, 2):
            for i in range(n - length + 1):
                total += prefix[i + length] - prefix[i]

        return total
