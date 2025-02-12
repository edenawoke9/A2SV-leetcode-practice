class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        total_sums = 0
        quantity = 1
        
        for i in range(len(nums)):
            total_sums += quantity * (nums[i] + nums[-i - 1])
            quantity = 2 * quantity - comb(i, k - 1)

        return total_sums % (10 ** 9 + 7)