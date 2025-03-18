class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        if n<1:
            return False
        n=n/3
        return self.isPowerOfThree(n)
        