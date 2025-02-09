class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        self.gain=gain
        alt=[0]*(len(gain)+1)
        for i in range(1,len(alt)):
            alt[i]=alt[i-1]+gain[i-1]
        return max(alt)