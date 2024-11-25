class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        self.aliceSizes = aliceSizes
        self.bobSizes = bobSizes

        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)

       
        diff = (sumAlice - sumBob) // 2

       
        aliceSet = set(aliceSizes)

       
        for b in bobSizes:
            a = b + diff
            if a in aliceSet:
                return [a, b]
